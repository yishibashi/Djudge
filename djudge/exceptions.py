class CompileError(Exception):
    def __init__(self, message):
        self.message = message


class RunnerError(Exception):
    def __init__(self, message):
        self.message = message
