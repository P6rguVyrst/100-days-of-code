
def null_decorator(func):
    return func

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Hey!'

x = greet()
print(x)


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'trace: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'trace: {func.__name__}() '
              f'returned {original_result}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

say('Toomas', 'Im hungry!')

import functools
def uppercase2(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase2
def greet():
    """documentation"""
    return 'asfagwegew'

print(greet())
print(greet.__name__)
print(greet.__doc__)



