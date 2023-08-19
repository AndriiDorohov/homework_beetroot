# Task 2
# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: 'start', 'end', and optional step. Tips:
# See the documentation for 'range' function

def in_range(start, end: int, step=1):
		i = 0
		r = []
		while (start + step * i) < end:
				r.append(start + step * i)
				i += 1
		return r

for num in in_range(1, 16):
		print(num)

for num in in_range(0, 10, 2):
    print(num)
