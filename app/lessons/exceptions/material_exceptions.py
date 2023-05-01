from app.base import AppException


class MaterialDoesNotExistsException(AppException):
    """Exception raised when no material found in Database."""
    message = "No material found."
    code = 404
