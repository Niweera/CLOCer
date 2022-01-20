import logging
import logging.config


class Logger:
    """
    Class to initiate Python Logging
    """

    def __init__(self) -> None:
        logging.config.dictConfig(
            config={
                "disable_existing_loggers": False,
                "version": 1,
                "formatters": {
                    "simple": {
                        "format": "[%(levelname).1s] [%(asctime)s] %(message)s",
                        "datefmt": "%d-%m-%Y %I:%M:%S %p",
                    }
                },
                "handlers": {
                    "default": {
                        "level": "INFO",
                        "formatter": "simple",
                        "class": "logging.StreamHandler",
                        "stream": "ext://sys.stdout",  # Default is stderr
                    },
                },
                "loggers": {
                    "": {
                        "handlers": ["default"],
                        "level": logging.INFO,
                    },
                },
            }
        )
