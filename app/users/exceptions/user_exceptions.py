from app.base import AppException


class InvalidPasswordForm(AppException):
    """Exception is raised when user's password form is not valid."""
    message = "Password must be at least 8 characters long with at least one number."
    code = 400


class InvalidVerificationCode(AppException):
    """Exception raised when user try to verify account with wrong verification code."""
    message = "Verification code unrecognized."
    code = 400


class AdminLoginException(AppException):
    """Exception is raised when user tries to log in as Admin."""
    message = "You are not an Admin."
    code = 403


class InvalidTokenException(AppException):
    """Exception raised on a wrong token authentication."""
    message = "Could not validate token."
    code = 403


class InvalidCredentialsException(AppException):
    """Exception raised on a wrong password during login action."""
    message = "Check your credentials."
    code = 401


class UnverifiedAccountException(AppException):
    """Exception raised when user tries to log in before account verification."""
    message = "Please verify your account first. Check your email for verification code."
    code = 401


class InactiveUserException(AppException):
    """Exception raised when user with inactive status tries to log in."""
    message = "Your account is inactive. Please contact our support team."
    code = 401
