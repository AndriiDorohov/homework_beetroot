# Task 4

# The name check.

# Write a program that has a variable with your name
# stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored
# name even if the given name has another case, e.g., if your input
# is “Anton” and the stored name is “anton”, it should return True.


def check_name(name, check):
   if name == check.lower():
       return True
   else:
       return False

user_name = "andrii"
input_name = input("Enter name: ")

print(check_name(user_name, input_name))
