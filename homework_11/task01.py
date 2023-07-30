# Task 1

# Write a Python program to detect the number of local variables declared in a function.

def create_variables():
    a = 1
    b = 2
    c = 3
    variables = locals()
    return print(len(variables))

create_variables()
