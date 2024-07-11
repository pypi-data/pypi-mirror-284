# DS-Toolkit

DS-Toolkit is a comprehensive collection of resources tailored for Data Science Services. Developed with the aim of enhancing productivity and ensuring best practices in data science projects, this toolkit encapsulates a variety of utilities and frameworks.

## Usage

### Example

```
from ds_toolkit.log import Fmt, get_logger

LOGGING_LEVEL = logging.DEBUG
adapter = get_logger("test_adapter", LOGGING_LEVEL, dict(imei="359206105981120"))
adapter.debug(
    Fmt(
        "fetching batch for device_data_{} between {} and {}",
        "359206105981120",
        "2024-07-09 08:35:42",
        "2024-07-09 08:45:42",
    )
)
adapter.info("HELLO %s", "WORLD")
```
Allowed context key-value pairs:
- imei: str
- packet_created_time: str
- packet_proccesed_time: str
- truck_id: str

## Development

### Getting Started

To get started with DS-Toolkit, ensure you have Python 3.11 or higher installed. Follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory and install dependencies using Poetry (if you do not have Poetry installed on your machine then visit https://python-poetry.org/docs/ and follow instructions):

```sh
poetry install
```

3. Activate the Poetry shell to work within the virtual environment in your terminal:

```sh
poetry shell
```

4. Run pre-commit install to set up the git hook scripts:

```sh
pre-commit install
```

### Authors
Lukas Benic - lukas@cloudcycle.com
