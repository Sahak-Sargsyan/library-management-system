class NotFoundException(Exception):
    pass

class DuplicateEmailException(Exception):
    pass

class AlreadyBorrowedException(Exception):
    def __init__(self, borrowed_data):
        self.borrowed_data = borrowed_data

class InvalidDataException(Exception):
    pass