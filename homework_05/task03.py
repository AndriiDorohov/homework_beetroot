# Task 3

# Extracting numbers.

# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible
# by 7 but not a multiple of 5, and store them in a separate
# list. Finally, print the list.

# Constraint: use only while loop for iteration

def fill_list(arg, val_1 = 7, val_2 = 5):
    i = 0
    new_list = []
    calc_list = []
    while i < arg:
        new_list.append(i+1)

        if (new_list[i] % val_1) == 0 and (new_list[i] % val_2) != 0:
            calc_list.append(new_list[i])

        i += 1
    return new_list, calc_list

integer_list, result = fill_list(100, 7, 5)
print(integer_list)
print(f"List that are divisible by 7 but not a multiple of 5: {result}")
