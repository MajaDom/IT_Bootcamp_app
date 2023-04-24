class GenerationNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class GenerationExists(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code