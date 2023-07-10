# Task 1

# The Guessing Game.

# Write a program that generates a random number
# between 1 and 10 and lets the user guess what
# number was generated. The result should be sent
# back to the user via a print statement.

# import random generate module
from random import randint

def generation_number():
     return randint(1, 10)

# The function of entering user response and comparing results
def check_answer(result):
    input_answer = input()
    if input_answer == str(result):
        print("Luck, you guessed it! :)")
    else:
        print(f"Unluck, you didn't guess it! :(. Number: {result}")

# Three simple mathematical expressions
print(f"Enter a number from 1 to 10 to test your luck: ")
result = generation_number()
check_answer(result)
