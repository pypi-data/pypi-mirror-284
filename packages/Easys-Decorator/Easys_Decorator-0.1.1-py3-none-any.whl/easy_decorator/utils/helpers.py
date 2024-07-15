import inspect

def get_function_args(func):
    return inspect.signature(func).parameters

def get_function_return_annotation(func):
    return inspect.signature(func).return_annotation