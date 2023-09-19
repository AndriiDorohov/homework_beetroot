# #!/usr/bin/env python3

# Task 1

# Write a program that reads in a sequence of characters
# and prints them in reverse order, using your implementation of Stack.

# Python program to reverse a string using stack

# Function to create an empty stack.
# It initializes size of stack as 0

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def is_empty(self):
        return not bool(self._items)

    def reverse(self, string):
        for char in string:
            self.push(char)
        reversed_string = ''
        while not self.is_empty():
            reversed_string += self.pop()
        return reversed_string

if __name__ == "__main__":
    s = Stack()
    input_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    reversed_string = s.reverse(input_string)
    print("Original string is: ", input_string)
    print("Reversed string is: ", reversed_string)
