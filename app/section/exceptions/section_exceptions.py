class SectionNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class SectionExists(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code