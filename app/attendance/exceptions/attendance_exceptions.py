class AttendanceNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class AttendanceExists(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code