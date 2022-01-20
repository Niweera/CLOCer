from typing import Union


class CloneError(Exception):
    def __init__(self, message: Union[Exception, str]) -> None:
        self.message: Union[Exception, str] = message
        super().__init__(self.message)


class ConfigureError(Exception):
    def __init__(self, message: Union[Exception, str]) -> None:
        self.message: Union[Exception, str] = message
        super().__init__(self.message)


class CLOCerError(Exception):
    def __init__(self, message: Union[Exception, str]) -> None:
        self.message: Union[Exception, str] = message
        super().__init__(self.message)
