# Task 2

# Write a function that takes in two numbers from
# the user via input(), call the numbers a and b,
# and then returns the value of squared a divided by
# b, construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def calc_val(a, b, *arg):
    return a * a / b

str_a = input("Input a & b with space: ").split()

try:
     int_b = [int(x) for x in str_a]
     if int_b[1] == 0:
          print('ZeroDivisionError - cannot divide by zero')
     else:
          print(calc_val(*int_b))

except ValueError:
     print('You entered a non-numeric value')
