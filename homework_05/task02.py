# Task 2

# Exclusive common numbers.

# Generate 2 lists with the length of 10 with
# random integers from 1 to 10, and make a third
# list containing the common integers between the 2
# initial lists without any duplicates.

# Constraints: use only while loop and random module
# to generate numbers

from random import randint


def generate_list(value = 10, length = 10):
    i = 0
    new_list = []
    while i < length:
        new_list.append(randint(1, value))
        i += 1
    print(new_list)
    return new_list


first_list = set(generate_list(10, 10))
second_list = set(generate_list(10, 10))
third_list = list(set.intersection(first_list, second_list))
print(f"List with intersection: {third_list}")
