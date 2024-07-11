import logging
from typing import TypedDict

from ds_toolkit.log.fmt import Fmt
from ds_toolkit.log.json_log_formatter import JSONLogFormatter


class AllowedContext(TypedDict, total=False):
    """
    Defines the structure of the allowed context for logging.

    Attributes:
        imei (str): The IMEI number of the device.
        packet_created_time (str): The creation time of the packet.
        packet_proccesed_time (str): The processed time of the packet.
        truck_id (str): The ID of the truck.
    """

    imei: str
    packet_created_time: str
    packet_proccesed_time: str
    truck_id: str


class ContextLoggerAdapter(logging.LoggerAdapter):
    """
    A custom logger adapter to include additional context in log messages.

    Attributes:
        logger (logging.Logger): The underlying logger instance.
        context (AllowedContext): The context to be included in log messages.
    """

    def __init__(self, logger, context: AllowedContext):
        """
        Initializes the ContextLoggerAdapter with a logger and context.

        Args:
            logger (logging.Logger): The underlying logger.
            context (AllowedContext): The context to be included in log messages.

        Raises:
            ValueError: If the context contains keys not allowed in AllowedContext.
        """
        allowed_keys = AllowedContext.__annotations__.keys()
        if not all(key in allowed_keys for key in context.keys()):
            raise ValueError("Context contains keys not allowed in AllowedContext")
        super().__init__(logger, context)

    def add_context(self, context: AllowedContext):
        """
        Adds additional context to the logger, ensuring it's allowed.

        Args:
            context (AllowedContext): The context to add.
        """
        allowed_keys = AllowedContext.__annotations__.keys()
        if not all(key in allowed_keys for key in context.keys()):
            raise ValueError("Context contains keys not allowed in AllowedContext")
        self.extra.update(context)

    def remove_context(self, key: str):
        """
        Removes a context key from the logger.

        Args:
            key (str): The key to remove.
        """
        if key in self.extra.keys():
            del self.extra[key]

    def replace_context(self, new_context: AllowedContext):
        """
        Replaces the current context with a new one, ensuring it's allowed.

        Args:
            new_context (AllowedContext): The new context to set.
        """
        allowed_keys = AllowedContext.__annotations__.keys()
        if not all(key in allowed_keys for key in new_context.keys()):
            raise ValueError("New context contains keys not allowed in AllowedContext")
        self.extra = new_context

    def log(self, level, msg, /, *args, stacklevel=1, **kwargs):
        """
        Logs a message with the given level, message, and additional arguments.

        Args:
            level (int): The log level for the message.
            msg (str): The log message.
            *args: Variable length argument list.
            stacklevel (int, optional): The stack level for the message. Defaults to 1.
            **kwargs: Arbitrary keyword arguments.
        """
        if self.isEnabledFor(level):
            msg, kwargs = self.process(msg, kwargs)
            self.logger.log(level, msg, *args, **kwargs, stacklevel=stacklevel)


def get_logger(name: str, level: str, context: AllowedContext = {}):
    """
    Creates and returns a ContextLoggerAdapter with the specified name, level, and context.

    Args:
        name (str): The name of the logger.
        level (str): The logging level.
        context (AllowedContext, optional): The context to include in log messages. Defaults to {}.

    Returns:
        ContextLoggerAdapter: The configured logger adapter.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Set a custom formatter
    formatter = JSONLogFormatter()
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    adapter = ContextLoggerAdapter(
        logger,
        context,
    )

    return adapter


if __name__ == "__main__":
    LOGGING_LEVEL = "DEBUG"

    adapter = get_logger("test_adapter", LOGGING_LEVEL, dict(imei="359206105981120"))

    # Example log messages
    adapter.debug(
        Fmt(
            "fetching batch for device_data_{} between {} and {}",
            "359206105981120",
            "2024-07-09 08:35:42",
            "2024-07-09 08:45:42",
        )
    )
    adapter.info("HELLO %s", "WORLD")
