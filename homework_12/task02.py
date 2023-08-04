# Task 2
# Write a decorator that takes a list of stop words and
# replaces them with * inside the decorated function

# def stop_words(words: list):
#     pass

# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
from functools import wraps

def stop_words(words: list):
     def decorator_inside(decorated_func):
         @wraps(decorated_func)
         def wrapper(name: str) -> str:
             result = decorated_func(name)
             for word in words:
             		result = result.replace(word, '*')
             print(result)
             return result
         return wrapper
     return decorator_inside

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
