from functools import wraps
# from sys import exit as __ex__

def once(func):
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
    """@twice decorator makes a function only usable twice~!"""
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

