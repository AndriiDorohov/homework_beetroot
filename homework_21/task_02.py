# #!/usr/bin/env python3

# Task 2

# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly
# brackets are "balanced."

class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

def is_balanced(expression, stack):
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or stack.pop() != bracket_pairs[char]:
                return False

    return stack.is_empty()

if __name__ == "__main__":
    stack1 = Stack()
    text = "Australia’s Parliament House (architects Mitchell/Giurgola & Thorp [New York]) opened on 9 May 1988."
    print(text)
    result = is_balanced(text, stack1)

    if result == True:
        print("Text is balanced")
    else:
        print("Text isn't balanced")
