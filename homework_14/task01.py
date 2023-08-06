# Task 1
# School
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and
# another one called Teacher. Try to find as many methods and
# attributes as you can which belong to different classes, and
# keep in mind which are common and which are not. For example,
# the name should be a Person attribute, while salary should only
# be available to the teacher.

student_data = ["Alice", "Smith", 20, "Female", "123 Main St", "alice@example.com", "Computer Science", 2, "Dorm A"]

class Person:
		def __init__(self, firstname: str, lastname: str, age: int, gender: str, address: str, email: str):
			self.firstname = firstname
			self.lastname = lastname
			self.age = age
			self.gender = gender
			self.address = address
			self.email = email

class Student(Person):
		def __init__(self, firstname: str, lastname: str, age: int, gender: str, address: str, email: str, faculty: str, course: int, dormitory: str):
			super().__init__(firstname, lastname, age, gender, address, email)
			self.faculty = faculty
			self.course = course
			self.dormitory = dormitory

class Teacher(Person):
		def __init__(self, firstname: str, lastname: str, age: int, gender: str, address: str, email: str, salary: float, subject: str, auditory: str):
			super().__init__(firstname, lastname, age, gender, address, email)
			self.__salary = salary
			self.subject = subject
			self.auditory = auditory

		@property
		def salary(self):
				print("Access to the salary is denied.")
				return None

student1 = Student("Rebeca", "Black", 19, "Female", "43 Flower St", "rebeca@gmail.com", "Philosophy", 2, "Dorm A")
print(f"Student: {student1.firstname} {student1.lastname}")
print(f"Faculty: {student1.faculty}")

teacher1 = Teacher("Dr. Mark", "Stoun", 35, "Male", "6 Park Ave", "mark@gmail.com", 32000, "Math", "Room 51")
print(f"Teacher: {teacher1.firstname} {teacher1.lastname}")
print(f"Salary:  {teacher1.salary} SEK")
