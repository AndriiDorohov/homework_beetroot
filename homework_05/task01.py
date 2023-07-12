# Task 1

# The greatest number

# Write a Python program to get the largest number
# from a list of random numbers with the length of 10

# Constraints: use only while loop and random module
# to generate numbers

from random import randint

def max_number(arg):
    i = 0
    new_list = []

    while i < arg:
        new_list.append(randint(1, arg))
        i += 1

    print(new_list)
    return new_list

max(max_number(10))
