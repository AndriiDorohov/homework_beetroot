class Programmer:
		def __init__(self, name: str, age: int, gender: str, stage: int) -> None:
				self.name = name
				self.age = age
				self.gender = gender
				self.stage = stage

		def work_experience(self):
				print(f"{self.name} has {self.stage} of work experience and works for the company")


class Junior(Programmer):
		def __init__(self, name: str, age: int, gender: str, stage: int) -> None:
			super().__init__(name, age, gender, stage)

		def work_experience(self):
				print(f"{self.name} has {self.stage} of work experience and works for the Microsoft company")


class Middle(Programmer):
		def __init__(self, name: str, age: int, gender: str, stage: int) -> None:
						super().__init__(name, age, gender, stage)
		def work_experience(self):
				print(f"{self.name} has {self.stage} of work experience and works for the Facebook company")

class Senior(Programmer):
		def __init__(self, name: str, age: int, gender: str, stage: int) -> None:
						super().__init__(name, age, gender, stage)
		def work_experience(self):
				print(f"{self.name} has {self.stage} of work experience and works for the Google company")

class TeamLead(Programmer):
		def __init__(self, name: str, age: int, gender: str, stage: int) -> None:
						super().__init__(name, age, gender, stage)
		def work_experience(self):
				print(f"{self.name} has {self.stage} of work experience and works for the Amazon company")

junior = Junior("Robert", 25, "Male", 1)
middle = Middle("Rebecca", 35, "Female", 2)
senior = Senior("Maxus", 28, "Male", 10)
team_Lead = TeamLead("Rita", 40, "Female", 15)
junior.work_experience()
middle.work_experience()
senior.work_experience()
team_Lead.work_experience()
