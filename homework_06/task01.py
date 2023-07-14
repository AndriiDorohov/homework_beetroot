# Task 1

# Make a program that has some sentence (a string)
# on input and returns a dict containing all unique
# words as keys and the number of occurrences as values.

# перебрати кортеж, на ітерації узяти елемент з кортежу, перевірити його входження у список і додати до словника

def build_tulip(arg):
    for x in arg:
        item_dict.update({x: item_list.count(x)})

item_str = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose."

# видаляємо коми і крапки та приводимо слова до єдиного реєстру
item_list = item_str.replace(",", "").replace(".", "").lower().split()
item_tuple = set(item_list)
item_dict = {}

build_tulip(item_tuple)

print(item_str)
print("-------------------------------------")
print(item_list)
print("-------------------------------------")
print(item_tuple)
print("-------------------------------------")
print(item_dict)
