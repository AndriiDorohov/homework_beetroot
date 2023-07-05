# Task 1

# String manipulation

# Write a Python program to get a string made of the first 2 and
# the last 2 chars from a given string. If the string length
# is less than 2, return instead of the empty string.

# Sample String: 'helloworld'
# Expected Result : 'held'
# Sample String: 'my'
# Expected Result : 'mymy'
# Sample String: 'x'
# Expected Result: Empty String

# Tips:
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and
# negative indexing to get the last characters

str_item = input("Input the text: ")
result = ""

if len(str_item) < 2:
    result = "Result: Empty String"
elif len(str_item) == 2:
    result =  f"Result: {str_item}{str_item}"
elif len(str_item) >= 4:
    result = f"Result: {str_item[0:2]}{str_item[-2:]}"


print(result)
