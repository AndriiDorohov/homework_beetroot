# #!/usr/bin/env python3

# Task 1

# File Context Manager class

# Create your own class, which can behave like a built-in function 'open'.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of '__exit__' method,
# which has to cover all the requirements to context managers mentioned
# here:

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()


# 'r'
# open for reading (default)
# 'w'
# open for writing, truncating the file first
# 'x'
# open for exclusive creation, failing if the file already exists
# 'a'
# open for writing, appending to the end of file if it exists
# 'b'
# binary mode
# 't'
# text mode (default)
# '+'
# open for updating (reading and writing)
