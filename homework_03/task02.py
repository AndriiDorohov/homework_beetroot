# Task 2

# The valid phone number program.

# Make a program that checks if a string is in the right
# format for a phone number. The program should check that
# the string contains only numerical characters and is only
# 10 characters long. Print a suitable message depending on
# the outcome of the string evaluation.

number_phone=""

while True:
    number_phone = input("Input the phone nuber:  ")
    if number_phone.isdigit() and len(number_phone) == 10:
        break
    else:
        print("Error, the phone number must consist of 10 digits")

print(f"You enter correct phone number:  {number_phone}")
