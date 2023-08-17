# Task 3
# Write a class TypeDecorators which has several methods for converting
# results of functions to a specified type (if it's possible):

# methods:
# to_int
# to_str
# to_bool
# to_float

# Don't forget to use @wraps

# class TypeDecorators:
#     pass

# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string

# @TypeDecorators.to_bool
# def do_something(string: str):
#     return string

# assert do_nothing('25') == 25
# assert do_something('True') is True

from functools import wraps

class TypeDecorators:

		@staticmethod
		def to_int(func):
				@wraps(func)
				def wrapper(*args, **kwargs):
						result = func(*args, **kwargs)
						result = int(result)
						print(f"type return {type(result)}")
						return result
				return wrapper

		@staticmethod
		def to_str(func):
				@wraps(func)
				def wrapper(*args, **kwargs):
						result = func(*args, **kwargs)
						result = str(result)
						print(f"type return {type(result)}")
						return result
				return wrapper

		@staticmethod
		def to_bool(func):
				@wraps(func)
				def wrapper(*args, **kwargs):
						result = func(*args, **kwargs)
						if result == "True":
							result = True
							print(f"type return {type(result)}")
							return result
						elif result == "False":
							result = False
							print(f"type return {type(result)}")
							return result
						else:
							raise ValueError("Input incorrect")
				return wrapper

		@staticmethod
		def to_float(func):
				@wraps(func)
				def wrapper(*args, **kwargs):
						result = func(*args, **kwargs)
						result = float(result)
						print(f"type return {type(result)}")
						return result
				return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
		return string

@TypeDecorators.to_bool
def do_something(string: str):
		return string

@TypeDecorators.to_str
def convert_to_string(number: int):
    return number

@TypeDecorators.to_float
def convert_to_float(string: str):
    return string

print(do_nothing('25')) # = 25
print(do_something('True')) # is True
print(convert_to_float('25')) # = 25.0
print(convert_to_string(25)) # = "25"
