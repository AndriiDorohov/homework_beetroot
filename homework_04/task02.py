# Task 2

# The birthday greeting program.

# Write a program that takes your name as input, and
# then your age as input and greets you with the following:

# “Hello <name>, on your next birthday you’ll be <age+1> years”

def user_details():
    global user_name, user_age
    user_list = input("Enter your name and age separated by a space").split()
    return (user_list[0], int(user_list[1]))

user_name, user_age = user_details()
print(f"Hello {user_name}, on your next birthday you’ll be {user_age + 1} years")
