# #!/usr/bin/env python3

# Task 3 (Optional)

# Pytest fixtures with context manager

# Create a simple function, which performs any logic of
# your choice with text data, which it obtains from a file object,
# passed to this function ( def test(file_obj) ).

# Create a test case for this function using pytest library
# (Full pytest documentation).

# Create pytest fixture, which uses your implementation of
# the context manager to return a file object, which could
# be used inside your function.


def process_text_data(file_obj):
    data = file_obj.read()
    uppercase_data = data.upper()
    print(uppercase_data)


with open("example.txt", "r") as file:
    process_text_data(file)
