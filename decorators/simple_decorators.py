import functools

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice



def do_twice_with_args(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


def do_twice_with_return(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


def do_twice_introspection(func):
    @functools.wraps(func)
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice