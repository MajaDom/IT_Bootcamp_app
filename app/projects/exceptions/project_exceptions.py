"""Project Exceptions"""


class ProjectNotFoundException(Exception):
    """Exception is raised when project is not found"""

    def __int__(self, message, code):
        self.message = message
        self.code = code
