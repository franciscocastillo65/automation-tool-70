class CustomError(Exception):
    """Base class for all exceptions raised by the automation tool."""
    pass

class ConfigurationError(CustomError):
    """Raised when there is a configuration issue."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FileNotFoundError(CustomError):
    """Raised when a required file is not found."""
    def __init__(self, filename):
        self.filename = filename
        self.message = f'File {self.filename} not found.'
        super().__init__(self.message)

class ValidationError(CustomError):
    """Raised when input validation fails."""
    def __init__(self, field, message):
        self.field = field
        self.message = f'Validation failed for {self.field}: {message}'
        super().__init__(self.message)