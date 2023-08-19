# Task 1
# Create your own implementation of a built-in function enumerate,
# named 'with_index', which takes two parameters: 'iterable' and 'start',
# default is 0. Tips: see the documentation for the enumerate function

def with_index(iterable = 0, start = 0):
		n = start
		for elem in iterable:
				yield n, elem
				n += 1

for i, num in with_index(range(5, 10), start=5):
		print(i, num)

fruits = ['apple', 'banana', 'cherry', 'date']
for i, fruit in with_index(fruits, start=3):
		print(i, fruit)

text = "Hello, World!"
for i, char in with_index(text, start=1):
		print(i, char)
