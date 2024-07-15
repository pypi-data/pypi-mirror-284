class EventPublishingException(Exception):
    """Base exception for errors encountered while publishing events."""
    pass


class InitializationException(Exception):
    """Raised when there is an error during the initialization of the analytics SDK."""
    pass


class InvalidEventException(EventPublishingException):
    """Raised when an event is invalid or missing required data."""
    pass
