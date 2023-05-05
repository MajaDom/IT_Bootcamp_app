class UserProjectNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserProjectExists(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code