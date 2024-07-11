import json
import logging


class JSONLogFormatter(logging.Formatter):
    """
    A formatter for converting log records to JSON format.

    This formatter is designed to serialize log records into JSON strings, facilitating
    easier parsing and processing of log data in systems that consume JSON. It is capable
    of including both standard and custom attributes within the log record, such as 'imei',
    'packet_created_time', and 'packet_processed_time'.

    Attributes:
        Inherits all attributes from the logging.Formatter class.

    Methods:
        format(record): Serializes the log record to a JSON string.
    """

    def format(self, record: logging.LogRecord):
        """
        Serializes the log record to a JSON string.

        Overrides the base class's format method to create a JSON representation of the log
        record. This includes both the standard attributes of a log record and any additional
        custom attributes that have been added to the record.

        Args:
            record (logging.LogRecord): The log record to serialize.

        Returns:
            str: The JSON string representation of the log record.
        """
        log_record = {
            "message": record.getMessage(),
        }
        if hasattr(record, "imei"):
            log_record["imei"] = record.imei

        if hasattr(record, "packet_created_time"):
            log_record["packet_created_time"] = record.packet_created_time

        if hasattr(record, "packet_processed_time"):
            log_record["packet_processed_time"] = record.packet_processed_time

        return json.dumps(log_record)
