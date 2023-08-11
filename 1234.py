# cтворити клас Student, який має два базових атрибути що описують студента,
# property що повертає його повне ім'я, staticmethod який для кожного студента
# повертає один і той самий університет, а також classmetod який повертає назву
# класу та повне ім'я студента. Бонус: створити документаційний рядок та
# вивести його.

class Student:
		university = "KPI"
		def __init__(self, first_name: str, last_name: str, age: int, uiversity: str) -> None:
			self.first_name = first_name
			self.last_name = last_name
			self.university = uiversity

		@property
		def full_name(self):
			return f"{self.first_name} {self.last_name}"

		@staticmethod
		def get_university():
			return Student.university

		@classmethod
		def get_class_and_full_name(cls, first_name, last_name):
			return f"Class: {cls.__name__}, Full Name: {first_name} {last_name}"

student1 = Student("Max", "Robinson", 19, "Politechnik")
print("University:", student1.university)
print("@static method:", Student.get_university())
print(student1.full_name)
print("Class and Full Name:", Student.get_class_and_full_name(student1.first_name, student1.last_name))
