class UserGenerationNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserGenerationExists(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code