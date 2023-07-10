# Task 3

# Words combination

# Create a program that reads an input string and
# then creates and prints 5 random strings from
# characters of the input string.

# For example, the program obtained the word ‘hello’,
# so it should print 5 random strings(words) that combine
# characters

# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)
from random import sample

def generate_random_words(arg):
    arg_list = list(arg)
    print(arg)
    for x in range(len(arg_list)):
        gen = sample(arg_list, len(arg_list))
        print("".join(gen))


primary_word = input("Enter a word and press Enter:   ")
generate_random_words(primary_word)

# P.S. The code does not include a check for duplicate combinations.
# Therefore, occasionally, similar generated variations may occur.
