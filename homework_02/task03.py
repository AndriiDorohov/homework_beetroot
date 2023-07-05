# Task 3
#
# Using python as a calculator.
#
# Make a program with 2 numbers saved in separate variables
# a and b, then print the result for each of the following:
#
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division

while True:
    a = input('Enter a value:')
    b = input('Enter b value:')
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        break

print(f"Addition a & b:         {(a+b)}")
print(f"Subtraction a & b:      {(a-b)}")
print(f"Division a & b:         {(a/b)}")
print(f"Multiplication a & b:   {(a*b)}")
print(f"Exponent (Power) a & b: {(a**b)}")
print(f"Modulus a & b:          {(a%b)}")
print(f"Floor division a & b:   {(a//b)}")
