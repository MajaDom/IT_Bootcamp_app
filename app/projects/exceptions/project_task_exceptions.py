"""Project Task Exceptions"""


class ProjectTaskNotFoundException(Exception):
    """Exception is raised when project task is not found"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
