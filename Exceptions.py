from deprecated import deprecated

class UserNotFoundException(Exception):
    pass

class UnexpectedLogicException(Exception):
    pass

class RestrictedActionException(Exception):
    pass