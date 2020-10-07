def custom_decorator(func):
    def wrapper():
        print("The function has not run yet.")
        func()
        print("The function has run successfully")
    return wrapper()


@custom_decorator
def print_hello():
    print("Hello world!")


if __name__ == '__main__':
    # This is the actual call... there is no function call.
    print_hello
