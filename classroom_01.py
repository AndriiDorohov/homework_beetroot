# Develop a program for student enrollment tracking at a university.
# The program should include a class called "University" and a class
# called "Student." The "University" class should have a budget (private variable),
# a list of available majors, and a list of attached students. The "Student" class
# should have a name, the major they are studying, a list of grades, and the
# presence of a scholarship, which should be made protected and private, respectively.

# In the "University" class, add a method that accepts a student for enrollment
# and allocates funds for them. Also, add a method to receive funding from sponsors.

# In the "Student" class, create getters and setters for grades (retrieving the l
# ist and adding a new grade with a limit on the number of grades).

# As an example of application, create instances of the "University" and "Student"
# classes and apply the methods to them.

class Student:
		def __init__(self, name: str, specialty: str, grades_list: list = [], has_scholarship: bool = False) -> None:
			self.name = name
			self.specialty = specialty
			self._grades_list = grades_list
			self.__has_scholarship = has_scholarship
# додавання нової оцінки
		def add_grade(self, grade: int):
			if len(self._grades_list) < 5:
				self._grades_list.append(grade)
			else:
				print("The list of grades is filled, new grades will not be added.")

# отримання списку оцінок
		def get_grades_list(self):
			return self._grades_list

# форматування для друку
		def __str__(self):
			return f"Name: {self.name}\nSpecialty: {self.specialty}\nGrades: {self._grades_list}\nHas Scholarship: {self.__has_scholarship}"

class University:
		def __init__(self, budget: int, available_specialties: list, attached_students: list = []) -> None:
			self.__budget = budget
			self.available_specialties = available_specialties
			self.attached_students = attached_students

# приймає студента на навчання та виділяює на нього кошти. Відбувається перевірка на наявність спеціальності
		def add_student(self, student: Student):
			if student.specialty in self.available_specialties:
				self.attached_students.append(student.name)
				self.__budget += 1500
			else:
				print(f"Specialty '{student.specialty}' is not available in thе university.")
# метод що приймає фінансування від меценатів
		def receive_donation(self, amount: int):
			self.__budget += amount
# форматування для друку
		def __str__(self):
			return f"Budget: {self.__budget}\nSpecialities list: {self.available_specialties}\nAttached students: {self.attached_students}\n"


student1 = Student("Philip Robinson", "Philosophy", [10, 8, 12], True)
print(student1)
print(f"Grades list for student {student1.name}: {student1.get_grades_list()}")
print("------------------------------------------------")
student2 = Student("Alice Douglas", "Cyber Security", [])
student3 = Student("Gina Tricot", "Biology", [])
student2.add_grade(6)
student2.add_grade(10)
student2.add_grade(4)
student2.add_grade(10)
student2.add_grade(10)
student2.add_grade(9) # Не буде додано, бо перевищує кількість оцінок у списку
print(student2)
print("------------------------------------------------")
university = University(9999, ["Philosophy", "Mathematics", "Computer Science", "Physics", "Biology"], ["Mark Wahlberg"])
university.add_student(student1)
university.receive_donation(1000000)
university.add_student(student2) # Не буде доданий, бо в університеті відсутня його спеціальність
university.add_student(student3)
print(university)
