class AutoClickerError(Exception):
    """Base class for exceptions in the AutoClicker tool."""
    pass

class ClickError(AutoClickerError):
    """Exception raised for errors related to clicking actions."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class ConfigurationError(AutoClickerError):
    """Exception raised for configuration-related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidActionError(AutoClickerError):
    """Exception raised when an invalid action is performed."""
    def __init__(self, action: str) -> None:
        message = f"Invalid action attempted: {action}"
        super().__init__(message)

class ResourceNotFoundError(AutoClickerError):
    """Exception raised when a required resource is not found."""
    def __init__(self, resource: str) -> None:
        message = f"Resource not found: {resource}"
        super().__init__(message)