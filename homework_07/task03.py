# Task 3

# A simple calculator.

# Create a function called make_operation, which
# takes in a simple arithmetic operator as a first
# parameter (to keep things simple let it only be '+', '-' or '*')
# and an arbitrary number of arguments (only numbers) as the
# second parameter. Then return the sum or product of all the
# numbers in the arbitrary parameter. For example:

# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42

def make_operation(operator, *args):
    if operator == "+":
        return sum(list(args))
    elif operator == "-":
        result = args[0]
        for x in args[1:]:
            result += -(x)
        return result
    elif operator == "*":
        result = 1
        for x in args:
            result *= x
        return result

print(make_operation('+', 7, 7, 2))        # should return 16
print(make_operation('-', 5, 5, -10, -20)) # should return 30
print(make_operation('*', 7, 6))           # should return 42
