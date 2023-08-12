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
