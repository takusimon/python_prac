#define the decorator function

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print('After funcition execution')
    return wrapper

@my_decorator
def say_hello():
    print('Hello, Decorators!')

say_hello()
        