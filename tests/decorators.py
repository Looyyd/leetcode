def log_decorator(func):
    def wrapper():
        print(f"{func.__name__} is being called.")
        func()
        print(f"{func.__name__} has finished.")
    return wrapper

@log_decorator
def say_hello():
    print("Hello!")

say_hello()
