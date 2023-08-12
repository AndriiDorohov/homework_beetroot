# Task 2

# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance
# of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped
# by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by
# he specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount
# of all existing books

# class Library:
#     pass

# class Book:
#     pass

# class Author:
#     pass

class Author:
		def __init__(self, name, country, birthday, books = []) -> None:
			self.name = name
			self.country = country
			self.birthday = birthday
			self.books_list = books

		def __str__(self):
			books_mod = ' '.join([f'"{item}"' for item in self.books_list])
			return f'AUTHOR:         {self.name},\nCOUNTRY:        {self.country},\nDATE OF BIRTH:  {self.birthday},\nBOOKS:          {books_mod}\n'

		def __repr__(self):
			books_mod = ' '.join([f"'{item}'" for item in self.books_list])
			return f"Author(name='{self.name}', country={self.country}, year={self.birthday}, books='{books_mod}')"

class Book:
		total_books = 0

		def __init__(self, name, year, author: Author) -> None:
			self.name = name
			self.year = year
			self.author = author
			Book.total_books += 1

		def __str__(self):
			return f"BOOK TITLE ADD: '{self.name}',\nYEAR:           {self.year},\n{self.author}"

		def __repr__(self):
			return f"Book(name='{self.name}', year={self.year}, author='{self.author}')"

class Library:
		def __init__(self,name, books = [], authors = []) -> None:
			self.name_lib = name
			self.books_list = books
			self.authors_list = authors

		def new_book(self, name: str, year: int, author: Author):
			book = Book(name, year, author)
			self.books_list.append(book)
			return book

		def group_by_author(self, author: Author):
			print(f"NAME AUTHOR FOR GROUP: {author.name}\n")
			for book in self.books_list:
				if book.author.name == author.name:
					print(f"FINISHED BOOK IN LIST:\n{book}\n")
			return author

		def group_by_year(self, year: int):
			gr = [book for book in self.books_list if book.year == year]
			for book in gr:
				print(f"SORTED BOOKS BY YEAR:\n{book}\n")
			return gr

		def __str__(self):
			books = "\n".join(str(book) for book in self.books_list)
			authors = "\n".join(str(author) for author in self.authors_list)
			return f"LIBRARY NAME: {self.name_lib},\nBOOKS ADDED:\n{books}\nCOLLECTION AUTORS:\n{authors}\n"

		def __repr__(self):
				return "You just called __repr__"


print("____________________Creation of the author's collection_______________________________")
author1 = Author("Stephen King", "USA", 1947, ["End of Watch", "Charlie the Choo-Choo", "Sleeping Beauties", "The Outsider", "The Institute", "If It Bleeds"])
author2 = Author("H. G. Wells", "England", 1866, ["Brynhild", "Star Begotten", "Apropos of Dolores", "The Brothers", "The Holy Terror", "Babes in the Darkling Wood", "All Aboard for Ararat", "You Can't Be Too Careful"])
author3 = Author("C. Robert Cargill", "USA", 1975, ["Sea of Rust", "Dreams and Shadows", "Queen of the Dark Things", "Day Zero"])
author4 = Author("Michel Thomas", "France", 1956, ["The Elementary Particles", "Platform"])
print(author1)
print(repr(author1))
print(author2)
print("__________________Creating a book_________________________________")
book1 = Book("The Camford Visitation", 2016, author2)
book2 = Book("11/22/63", 2011, author1)
print(book2)
book3 = Book("We Are Where the Nightmares Go", 2018, author3)
print(book1)
print(repr(book1))
print(book3)
print(f"NUMBER OF BOOKS ADDED: {Book.total_books}\n")
print("_____________________Create a list of library contents______________________________")
library = Library("Stadsbiblioteket", [book1, book2, book3], [author1, author2, author3])
print(library)
print("______________________Add new book_______________________________")
add_book = library.new_book("Soumission", 2015, author4)
print(add_book)

print("______________________Group books by author and year_______________________________")
grouped_by_author = library.group_by_author(author3)

grouped_by_year = library.group_by_year(2011)
