# #!/usr/bin/env python3

# Task 1

# File Context Manager class

# Create your own class, which can behave like a built-in function 'open'.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of '__exit__' method,
# which has to cover all the requirements to context managers mentioned
# here:
import os


class FileManager:
    counter = 0

    @classmethod
    def get_num_of_usage(cls):
        return cls.counter

    def __init__(self, file_name, method):
        self.file_name = open(file_name, method)
        self.file_path = file_name
        print(f"Open file")

    def __enter__(self):
        print(f"Entering context")
        FileManager.counter += 1
        return self

    def write_log(self, text):
        self.file_name.write(text)
        print(f"Writing text")

    def read_file(self):
        return self.file_name.read()

    def __exit__(self, type, value, traceback):
        print(f"Closing context, number of contexts is {FileManager.counter}")
        self.file_name.close()
        os.remove(self.file_path)


with FileManager("temp.txt", "w") as opened_file:
    print(
        "Call context manager instance method to get counter value:",
        FileManager.get_num_of_usage(),
    )
    opened_file.write_log("Hi")

with FileManager("temp.txt", "w") as opened_file:
    print(
        "Call context manager instance method to get counter value:",
        FileManager.get_num_of_usage(),
    )
    opened_file.write_log("Hello")
