from app.base import AppException


class HomeworkDoesNotExistsException(AppException):
    """Exception raised when no homework found in Database."""
    message = "No homework found."
    code = 404
