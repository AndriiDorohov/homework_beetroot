# Task 2

# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def main_func():
        msg = 'It is main_func'
        def inside_func():
                print (msg)
        return inside_func

my_func = main_func()
my_func()
