from functools import wraps
# from sys import exit as __ex__

def once(func):
    """@once decorator makes a function run only once!
    
    `usage`

    >>> from deny_me.restrict import once # import the once decorator.
    
    >>> class abc:
    ...     def __init__(self):
    ...         pass
    ...     @once
    ...     def function(self, *args, **kwargs):
    ...         # do something

    `Follow the above syntax to run any function in a class only once`

    `To call the function:`

    >>> class_obj = abc()
    >>> class_obj.function(...) # this will run
    >>> class_obj.function(...) # this will not run
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if hasattr(self, '_called_functions') and func.__name__ in self._called_functions:
            raise Exception(f"{func.__name__} can only be called once.")
        if not hasattr(self, '_called_functions'):
            self._called_functions = {}
        self._called_functions[func.__name__] = True
        return func(self, *args, **kwargs)
    return wrapper

def twice(func):
    """@twice decorator makes a function only usable twice~!

    `usage`

    >>> from deny_me.restrict import twice # import the twice decorator.

    >>> class abc:
    ...     def __init__(self):
    ...         pass
    ...     @twice
    ...     def function(self, *args, **kwargs):
    ...         # do something

    `Follow the above syntax to run any function in a class only twice.`

    `to run the function:`

    >>> class_obj = abc()
    >>> class_obj.function(...) # this will run
    >>> class_obj.function(...) # this will also run
    >>> # some code
    >>> class_obj.function(...) # this will not run
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Use a special attribute to track the number of times the function has been called
        if not hasattr(self, '_called_functions'):
            self._called_functions = {}
        
        call_count = self._called_functions.get(func.__name__, 0)
        
        if call_count >= 2:
            raise Exception(f"{func.__name__} can only be called twice.")
        
        self._called_functions[func.__name__] = call_count + 1
        return func(self, *args, **kwargs)
    return wrapper

class Allow:
    """`class Allow`: This class defines and implements a decorator that can make any function only run `n` times.
    where, `n` is `user-defined`.

    `usage`

    >>> # import the allow class
    >>> from deny_me.restrict import Allow

    >>> # use
    >>> class abc:
    ...    def __init__(self):
    ...        pass    
    ...    # this will run 5 times and no more.
    ...    @Allow(5).times
    ...    def function(self, *args, **kwargs):
    ...        # do something

    `Follow the above syntax to run any function n(5) times`

    `to run the function:`
    >>> class_obj = abc()
    >>> class_obj.function(...) # this can be repeated 4 times more.
    """
    def __init__(self, times: int) -> None:
        self.number = times
    
    def times(s, func):
        """This decorator extender makes sure any given function runs n times."""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, '_called_functions'):
                self._called_functions = {}
        
            call_count = self._called_functions.get(func.__name__, 0)
            
            if call_count >= s.number:
                raise Exception(f"{func.__name__} can only be called {s.number} times.")
            
            self._called_functions[func.__name__] = call_count + 1
            return func(self, *args, **kwargs)
        return wrapper