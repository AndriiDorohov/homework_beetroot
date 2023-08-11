# Task 3
# Fraction
# Create a class Fraction that represents the fundamental
# arithmetic logic for fractions (+, -, /, *) with appropriate
# error checking and handling. You need to add magic methods for
# mathematical operations and comparison operations between Fraction
# class objects.

# class Fraction:
#     pass

# if __name__ == "__main__":
#     x = Fraction(1, 2)
#     y = Fraction(1, 4)
#     x + y == Fraction(3, 4)

def gcd(m,n):
		while m%n != 0:
				oldm = m
				oldn = n
				m = oldn
				n = oldm%oldn
		return n

class Fraction:
		def __init__(self, top, bottom):
			if not isinstance(top, int) or not isinstance(bottom, int):
				raise ValueError("Wrong data type")
			if bottom == 0:
				raise ValueError("You can't divide by zero")
			self.num = top
			self.den = bottom

		def __str__(self):
			return str(self.num)+"/"+str(self.den)

		def __add__(self, otherfraction):
			newnum = self.num*otherfraction.den + self.den*otherfraction.num
			newden = self.den * otherfraction.den
			common = gcd(newnum,newden)
			return Fraction(newnum//common,newden//common)

		def __mul__(self, otherfraction):
			newnum = self.num * otherfraction.num
			newden = self.den * otherfraction.den
			common = gcd(newnum,newden)
			return 1 if (newnum == newden) else Fraction(newnum//common, newden//common)

		def __truediv__(self, otherfraction):
			newnum = self.num * otherfraction.den
			newden = self.den * otherfraction.num
			common = gcd(newnum,newden)
			return 1 if (newnum == newden) else Fraction(newnum//common, newden//common)

		def __eq__(self, otherfraction):
				firstnum = self.num * otherfraction.den
				secondnum = otherfraction.num * self.den
				return firstnum == secondnum

if __name__ == "__main__":
		x = Fraction(1, 2)
		y = Fraction(1, 4)
		a = Fraction(2, 5)
		b = Fraction(2, 5)
		print(f" {a} == {b} : {a == b}")
		print(f" {x} == {y} : {x == y}")
		# x + y == Fraction(3, 4)
		print(f" {x} + {y} = {x + y}")
		print(f" {a} * {b} = {a * b}")
		print(f" {a} / {b} = {a / b}")
