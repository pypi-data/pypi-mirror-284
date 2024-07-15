from functools import wraps

def decorator_factory(before=None, after=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if before:
                before(*args, **kwargs)
            result = func(*args, **kwargs)
            if after:
                after(result)
            return result
        return wrapper
    return decorator