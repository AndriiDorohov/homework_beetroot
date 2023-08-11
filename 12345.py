# Змоделювати поведінку "освітніх процесів". Використати модель
# персона-школяр-студент-працівник. В базовому класі реалізувати
# getter (отримання ім'я та ступеня) & setter (задання ступеня освіти),
# а в наступних класах при створенні (метод __new__) додати перевірку
# на отримання попереднього ступеня, в __init__ передаємо екземпляр класу

class Person:
		def __init__(self, name: str, level: int) -> None:
			self.name = name
			self.level = level

		def getx(self):
				return f"Name: {self.name} level: {self.level}"

		def setx(self, value):
				self.level = value

		def delx(self):
				del self._x

		our_property = property(getx, setx, delx, "Hi")

class Schoolboys:
		def __init__(self) -> None:
			pass

		def __new__(cls):
			pass

		def __str__(self) -> str:
			pass

class Students:
		def __init__(self, idNo, level) -> None:
			self.idNo = idNo
			self.level = level

		def __new__(cls, idNo, level):
			if 5 <= level <= 10:
				print("Creat")
				return super(Studens, cls).__new__(cls)
			else:
				return None

		def __str__(self) -> str:
			return '{0}({1})'.format(self.__class__.__name__, self.__dict__)

class Workers:
		def __init__(self) -> None:
			pass

		def __new__(cls):
			pass

		def __str__(self) -> str:
			pass

sudent1 = Students("John Rok", 6)
