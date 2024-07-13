from functools import wraps
from deny_me.exceptions import PasswordError, ProtectedError

class Password:
    """`class Password`: This class defines and implements a decorator that can make any function password protected.
    
    `usage`

    >>> from deny_me.password import Password # import the password class.

    >>> class abc:
    ...     def __init__(self):
    ...         pass
    ...     # define a function here.
    ...     @Password("pass123").protected
    ...     def function(self, *args, **kwargs):
    ...         # do something

    `Follow this syntax to make any function password protected inside a class`

    `to run:`
    >>> class_obj = abc()
    >>> class_obj.function(...) # this will give error.
    >>> class_obj.function(password="pass2323232", ...) # this will also give error.
    >>> class_obj.function(password="pass123", ...) # this will run.
    """
    def __init__(self, password: str):
        self.__password = password
    
    def protected(s, func):
        """This decorator extender is mainly responsible for protection."""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            password = kwargs.pop("password", None)
            if password != None:
                if password == s.__password:
                    return func(self, *args, **kwargs)
                else:
                    raise PasswordError("Wrong Password provided for an exclusive function.")
            else:
                raise ProtectedError("This function is not available.")
        return wrapper