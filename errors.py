class Error(Exception):
    """Base class for other exceptions"""
    pass

class LoggedInError(Error):
    pass

class ActivationError(Error):
    pass