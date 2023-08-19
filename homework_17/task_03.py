# Task 3
# Create your own implementation of an iterable, which could be used
# inside for-in loop. Also, add logic for retrieving elements using
# square brackets syntax.

class MyIterable:

		def __init__(self, _from, _to):
				self.ind = _from
				self.to = _to
				self.list_iter = []

		def __iter__(self):
				return self

		def __next__(self):
				if self.ind > self.to:
						raise StopIteration
				val = self.ind
				self.ind += 1
				self.list_iter.append(val)
				return val

		def __getitem__(self, index):
				if index < 0 or index >= len(self.list_iter):
						raise IndexError("Index out of range")
				return self.list_iter[index]

my_iterable = MyIterable(1, 19)
for item in my_iterable:
		print(item)

print(my_iterable[8])
