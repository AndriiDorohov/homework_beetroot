# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#  "add called with 4, 5"

# def logger(func):
#     pass

# @logger
# def add(x, y):
#     return x + y

# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]

def logger(func):
    def wrap(*args):
        func_name = func.__name__
        args_str = ', '.join(map(str, args))
        print(f"Function: {func_name}. Called with args {args_str}")
        return func(*args)
    return wrap

@logger
def add(x, y):
		return x + y

@logger
def square_all(*args):
		return [arg ** 2 for arg in args]

add(4, 5)
square_all(4, 5, 10, 99)
