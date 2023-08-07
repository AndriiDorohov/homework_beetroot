# Task 4
# Custom exception
# Create your custom exception named 'CustomException',
# you can inherit from base Exception class, but extend
# its functionality to log every error message to a file
# named 'logs.txt'. Tips: Use __init__ method to extend
# functionality for saving messages to file

# class CustomException(Exception):
# def __init__(self, msg):

class CustomException(Exception):
		def __init__(self, msg):
				super().__init__(msg)
				self.msg = msg

		def write_text(self):
				with open('logs.txt', 'a') as file:
						file.write(self.msg + '\n')

try:
		raise CustomException("Test Failures")
except CustomException as e:
		print("Error:", e.msg)
		e.write_text()

try:
		raise CustomException("Wrong input")
except CustomException as e:
		print("Error:", e.msg)
		e.write_text()
