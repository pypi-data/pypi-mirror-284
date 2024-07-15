class EasyDecoratorException(Exception):
    """Base exception class for all Easy-Decorator exceptions."""
    def __init__(self, message="An error occurred in Easy-Decorator"):
        self.message = message
        super().__init__(self.message)


class DecoratorError(EasyDecoratorException):
    """Base class for exceptions related to decorator usage."""
    def __init__(self, message="An error occurred while using a decorator"):
        super().__init__(message)


class InvalidDecoratorError(DecoratorError):
    """Raised when an invalid decorator is used or created."""
    def __init__(self, message="Invalid decorator used or created"):
        super().__init__(message)


class DecoratorArgumentError(DecoratorError):
    """Raised when there's an issue with decorator arguments."""
    def __init__(self, message="Invalid arguments provided to decorator"):
        super().__init__(message)


class AsyncDecoratorError(DecoratorError):
    """Raised for issues specific to async decorators."""
    def __init__(self, message="An error occurred in an async decorator"):
        super().__init__(message)


class RetryError(EasyDecoratorException):
    """Raised when a retry decorator exhausts all attempts."""
    def __init__(self, message="Retry decorator exhausted all attempts"):
        super().__init__(message)


class TimeoutError(EasyDecoratorException):
    """Raised when a timeout decorator exceeds the specified time limit."""
    def __init__(self, message="Operation timed out"):
        super().__init__(message)


class SingletonError(EasyDecoratorException):
    """Raised for issues related to the singleton decorator."""
    def __init__(self, message="An error occurred with the singleton decorator"):
        super().__init__(message)


class DeprecationWarning(Warning):
    """Warning raised by the deprecated decorator."""
    def __init__(self, message="This feature is deprecated"):
        self.message = message
        super().__init__(self.message)


class ValidationError(EasyDecoratorException):
    """Raised when input validation fails in a decorator."""
    def __init__(self, message="Input validation failed"):
        super().__init__(message)


class CacheError(EasyDecoratorException):
    """Raised for issues related to caching decorators."""
    def __init__(self, message="An error occurred with a caching decorator"):
        super().__init__(message)


class ThreadingError(EasyDecoratorException):
    """Raised for issues related to threading decorators."""
    def __init__(self, message="An error occurred in a threading decorator"):
        super().__init__(message)


class PermissionError(EasyDecoratorException):
    """Raised when a permission check fails in a decorator."""
    def __init__(self, message="Permission check failed"):
        super().__init__(message)


class RateLimitError(EasyDecoratorException):
    """Raised when rate limiting is exceeded."""
    def __init__(self, message="Rate limit exceeded"):
        super().__init__(message)


class LoggingError(EasyDecoratorException):
    """Raised for issues related to logging decorators."""
    def __init__(self, message="An error occurred in a logging decorator"):
        super().__init__(message)