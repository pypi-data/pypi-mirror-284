class ShelliumException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UserDataDirExistsError(ShelliumException):
    def __init__(self, message):
        super().__init__(message)


class UserDataBuildError(ShelliumException):
    def __init__(self, message):
        super().__init__(message)


class ShellDriverAlreadyRunningError(ShelliumException):
    def __init__(self, message):
        super().__init__(message)


class ShellDriverVersionError(ShelliumException):
    def __init__(self, message):
        super().__init__(message)
