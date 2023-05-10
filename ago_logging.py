
def log_decorator(version=None, message=None, log_level=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            # Do something with arg1 and arg2
            result = func(*args, **kwargs)
            # Do something after the function call
            return result
        return wrapper
    return my_decorator

class AGOLogger():
    
    def __init__(self, version=None, message=None, log_level=None):
        self.version = version
        self.message = message
        self.log_level = log_level

    def log(message):
        print(message)

    def exception(message):
        print(message)