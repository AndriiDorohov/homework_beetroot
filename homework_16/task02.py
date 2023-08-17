# Task 2
# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that
# allows you to add workers to a Boss. You're not allowed to add instances of Boss
# class to workers list directly via access to attribute, use getters and setters instead!
# You can refactor the existing code.

# id_ - is just a random unique integer

# class Boss:
#     def __init__(self, id_: int, name: str, company: str):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []

# class Worker:
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.boss = boss

def generate_id(counter=[1]):
		new_id = counter[0]
		counter[0] += 1
		return new_id

class Boss:
		def __init__(self, id_: int, name: str, company: str):
			self.id = id_
			self.name = name
			self.company = company
			self.workers = []

		@property
		def list_workers(self):
			return self.workers

		@list_workers.setter
		def list_workers(self, worker):
			if isinstance(worker, Worker):
				self.workers.append(worker)
			else:
				raise ValueError("The worker is not an instance of the Worker class")


class Worker:
		def __init__(self, id_: int, name: str, company: str, boss: Boss):
			self.id = id_
			self.name = name
			self.company = company
			self.boss = boss

boss1 = Boss(generate_id(), name="Javad", company="ABF")
boss2 = Boss(generate_id(), name="Casper", company="Marcus inc.")

worker1 = Worker(generate_id(), name="Martin", company="ABF", boss=boss1)
worker2 = Worker(generate_id(), name="Eva", company="Marcus inc.", boss=boss2)

boss1.list_workers = worker1
boss2.list_workers = worker2

# Виводимо інформацію про керівників та їх працівників
print(f"Boss 1: {boss1.name}, Company: {boss1.company}\nWorkers of Boss 1:" + "\n".join([f"  {worker.name}" for worker in boss1.list_workers]))

print(f"Boss 2: {boss2.name}, Company: {boss2.company}\nWorkers of Boss 2:" + "\n".join([f"  {worker.name}" for worker in boss2.list_workers]))
