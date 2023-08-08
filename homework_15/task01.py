# Task 1

# Method overloading.

# Create a base class named Animal with a method called talk and then
# create two subclasses: Dog and Cat, and make their own implementation
# of the method talk be different. For instance, Dog’s can be to print
# ‘woof woof’, while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input instance
# of a Cat or Dog classes and performs talk method on input parameter.

def zoo(obj):
		print(obj.talk())

class Animal:
		def talk(self):
			return f"{self.__class__.__name__} do not speak"

class Dog(Animal):
		def talk(self):
			return f"The {self.__class__.__name__} say: 'woof-woof'"

class Cat(Animal):
		def talk(self):
			return f"The {self.__class__.__name__} say: 'meow-meow'"

class Goat(Animal):
		def talk(self):
			return f"The {self.__class__.__name__} say: 'baa-baa'"

class Pig(Animal):
		def talk(self):
			return f"The {self.__class__.__name__} say: 'oink-oink'"

class Cow(Animal):
		def talk(self):
			return f"The {self.__class__.__name__} say: 'moo-moo'"

class Donkey(Animal):
		def talk(self):
			return f"The {self.__class__.__name__} say: 'hee-haw-hee-haw'"

class Chicken(Animal):
		def talk(self):
			return f"The {self.__class__.__name__} say: 'cock-a-doodle-do'"

class Owl(Animal):
		def talk(self):
			return f"The {self.__class__.__name__} say: 'hoot-hoot'"

animal_classes = {
		"dog": Dog,
		"cat": Cat,
		"goat": Goat,
		"pig": Pig,
		"cow": Cow,
		"donkey": Donkey,
		"chicken": Chicken,
		"owl": Owl
}

for animal_type in animal_classes:
	animal_class = animal_classes[animal_type]
	animal = animal_class()
	zoo(animal)
