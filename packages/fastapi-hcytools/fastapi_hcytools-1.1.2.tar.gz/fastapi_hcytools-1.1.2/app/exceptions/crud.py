# DB Error

class DBIntegrityError(Exception):
    """Raised when an integrity exception in the DB layer occurs"""
    def __init__(self, message):
        super(DBIntegrityError, self).__init__(message)
        self.message = message


class WrongObjectError(Exception):
    """Raised when trying to save, update or delete objects that the repository
    does not handle"""
    def __init__(self, message):
        super(WrongObjectError, self).__init__(message)
        self.message = message