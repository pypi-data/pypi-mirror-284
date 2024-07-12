from functools import wraps
from deny_me.exceptions import PasswordError, ProtectedError
from deny_me.restrict import once
# from sys import exit as __ex__

class Password:
    def __init__(self, password: str):
        self.__password = password
    
    def protected(s, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            password = kwargs.pop("password", None)
            if password != None:
                # __p = Password("")
                if password == s.__password:
                    return func(self, *args, **kwargs)
                else:
                    raise PasswordError("Wrong Password provided for an exclusive function.")
            else:
                raise ProtectedError("This function is not available.")
        return wrapper