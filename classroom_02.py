# Створити власний клас List та спробувати відтворити основні
# його властивості за допомогою dunder методів:
# 1. Конкатенацію __add__
# 2. Різницю списків __sub__
# 3. Обчислення довжини __len__
# 4. Отримання елемента за індексом __getitem__
# 5. Задання едемента за індексом __setitem__
# А також описати метод класу append який буде додавати елемент
# в список не на кінець, а на початок
import random

class List():
		def __init__(self, list1):
			self.list1 = list1
			print(self.list1)


		def __add__(self, list2):
			list3 = []
			for item1, item2 in zip(self.list1, list2.list1):
				list3.append(item1 + item2)
			return list3

		def __sub__(self, list2):
			list3 = tuple(self.list1 + list2.list1)
			return list(list3)

		def __len__(self):
			return len(self.list1)

		def __getitem__(self, index):
			return self.list1[index]

		def __append__(self, value):
			self.list1.insert(0, value)

		# def __str__(self):
		# 	return f''

list1 = List([random.randint(1, 100) for _ in range(3)])
list2 = List([random.randint(1, 100) for _ in range(3)])
list3 = list1 + list2
print(f"__add__:{list3}")
list4 = list1 - list2
print(f"__sub__:{list4}")
print(f"__len__:{len(list1)}")
list1.__append__(10)
print(f"__append__'10':{list1.list1}")
element = list1.__getitem__(1)
print(f"__getitem__: {element}")
