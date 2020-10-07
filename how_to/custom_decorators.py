import functools


def custom_decorator(func):
    # This decorator helps in clarifying the passed function's identity.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("The function has not run yet.")
        return_value = func(*args, **kwargs)
        # Just in case the function's return is needed.
        print("The function has run successfully")
        return return_value
    return wrapper()


@custom_decorator
def print_hello():
    print("Hello world!")


if __name__ == '__main__':
    # This is the actual call... there is no function call.
    print_hello
