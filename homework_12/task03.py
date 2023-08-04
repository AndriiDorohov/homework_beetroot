# Task 3
# Write a decorator "arg_rules" that validates arguments
# passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should
# return False and print the reason it failed; otherwise, return the result.

# def arg_rules(type_: type, max_length: int, contains: list):
#     pass
from functools import wraps
import re

def arg_rules(type_: type, max_length: int, contains: list):
		def decorator_inside(decorated_func):
				@wraps(decorated_func)
				def wrapper(arg):

						count = 0
						try:
							for s in contains:
								count = count + len(re.findall(s, arg))
						except:
							print("The string must contain the character:", contains)
							return False

						if type_ != type(arg):
								print("The types don't match", type_)
								return False
						elif max_length < len(arg):
								print("The string exceeds the maximum length", max_length)
								return False
						elif count != len(arg):
								print("The string contains unregistered characters")
								return False
						else:
								return decorated_func(arg)
				return wrapper
		return decorator_inside

@arg_rules(str, 15, ['a', 'b', 'c'])
def my_function(x):
		return x + x

result = my_function("abc")
print(result)

result = my_function("aabbccdd")
print(result)

result = my_function([1, 2, 3])
print(result)
