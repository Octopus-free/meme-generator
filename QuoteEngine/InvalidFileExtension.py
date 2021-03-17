
class InvalidFileExtension(Exception):

    def __init__(self, *args):
        self.default_message = 'The file is not suite'
        self.input_message = ''
        for value in args:
            self.input_message = value

    def __repr__(self):
        if len(self.input_message) != 0:
            return self.input_message
        else:
            return self.default_message



