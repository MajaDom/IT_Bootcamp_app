from app.base import AppException


class LessonDoesNotExistsException(AppException):
    """Exception raised when no lesson found in Database."""
    message = "No lesson found."
    code = 404
