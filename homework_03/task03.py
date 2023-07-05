# Task 3

# The math quiz program.

# Write a program that asks the answer for a mathematical
# expression, checks whether the user is right or wrong, and
# then responds with a message accordingly.

# import random generate module
from random import randint

# randomize numbers for expression
random_number1 = randint(1, 10)
random_number2 = randint(1, 10)
random_number3 = randint(1, 10)
input_answer = 0

# The function of entering user response and comparing results
def check_answer(result):
    input_answer = input()
    if input_answer == str(result):
        print("This is the right decision")
    else:
        print(f"This is the wrong decision. Answer: {result}")

# Three simple mathematical expressions
print(f"Enter the answer for:  {random_number1} + {random_number2} - {random_number3}")
result = random_number1 + random_number2 - random_number3
check_answer(result)

print(f"Enter the answer for:  {random_number1} * {random_number2} + {random_number3}")
result = random_number1 * random_number2 + random_number3
check_answer(result)

print(f"Enter the answer for:  {random_number1} - {random_number2} * {random_number3}")
result = random_number1 - random_number2 * random_number3
check_answer(result)
