# Task 3
# Product Store
# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products
# and will operate with all products in the store. All methods,
# in case they can’t perform its action, should raise ValueError
# with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing
# the ProductStore class. You can also implement additional classes
# to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product
# with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a
# discount for all products specified by input identifiers (type or name).
# The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of
# products from the store if available, in other case raises an error.
# It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available
# products in the store.
# get_product_info(product_name) - returns a tuple with product name and
# amount of items in the store.

# class Product:
#     pass
# class ProductStore:
# pass
# p = Product('Sport', 'Football T-Shirt', 100)
# p2 = Product(Food, 'Ramen', 1.5)
# s = ProductStore()
# s.add(p, 10)
# s.add(p2, 300)
# s.sell('Ramen', 10)
# assert s.get_product_info('Ramen') == ('Ramen', 290)

import json

data_cat = {}

class Product:
		def __init__(self, type: str, name: str, price: float) -> None:
			self.type = type
			self.name = name
			self.price = price

class ProductStore():
		revenue = 0  #Змінна для пірахунку загальної суми продажів через метод sell_product
		discount_counter = 0  #Змінна для зберігання дискоунту, який мі потім вирахуємо із загального прибутку з продажу

		def __init__(self) -> None:
			pass

		def add(self, product, amount):
			self.amount = amount
			if product.type not in data_cat:   #Додаєм новий розділ при відсутності
				data_cat[product.type] = [{"product": product.name, "amount": self.amount, "price": round((product.price * 1.3), 2)}]
			else:
				action_chk = False   #Якщо розділ присутній, шукаємо по ньому потрібні ключі
				for item in data_cat[product.type]:
					if item["product"] == product.name:
						item["amount"] += self.amount  #Збільшуємо кількість товару на вказане значення
						action_chk = True
						break
				if action_chk == False:  #Якщо вимикач не спрацював, значить товар у цьому розділі відсутній і ми його додаємо
					data_cat[product.type].append({"product": product.name, "amount": self.amount, "price": round((product.price * 1.3), 2)})


		def set_discount(self, identifier, percent, identifier_type="name"):
			self.percent = percent
			for item in data_cat[identifier]:   #Додаємо поле зі знижкою, щоб надалі порахувати дисконт
				if item['product'] == identifier_type:
					item['discount'] = self.percent
					break

		def sell_product(self, product_name, amount):
			self.amount = amount
			action_chk = False   #Лічильник для перевірки на наявність даного продукту
			for item in data_cat:  #Проходимся по категоріям
				for count in data_cat[item]:  #Проходимось по ключам у середині списків
					if count["product"] == product_name:
						count["amount"] -= self.amount  #Видаляємо продану кількість товару
						if count.get("discount", None) != None:  #При наявності ключа дисконту, вираховуємо процент дисконту з проданого товару
							self.discount_counter += self.amount * count["price"] * int(count["discount"][0:-1]) / 100
						self.revenue += self.amount * count["price"]  #Вираховуємо загальну суму продажу
						action_chk = True
						break
			if action_chk == False:
				print(f'The product "{product_name}" is not in the database')

		def get_income(self):  #Друкуємо загальну суму, потім із прибутку в 30% вираховуємо процент дисконту
			print(f'Total sales: {self.revenue} $ , total profit: {round((self.revenue * 0.3 - self.discount_counter), 2)} $')

		def get_all_products(self):  #Друкуємо базу даних
			print(f'All product: {json.dumps(data_cat, indent=4)}')

		def get_product_info(self, product_name):  #Виводимо інформацію по окремому товару
			action_chk = False
			for item in data_cat:
				for count in data_cat[item]:
					if count["product"] == product_name:
						print(f'The product "{product_name}" : {count["amount"]} pc')
						action_chk = True
						break
			if action_chk == False:
				print(f'The product "{product_name}" is not in the database')

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 10.5)
p3 = Product('Food', 'Milk', 35)
p4 = Product('Electronic', 'Toster', 200)
p5 = Product('Electronic', 'Sub Woofer', 750)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.add(p3, 111)
s.add(p2, 99)
s.add(p2, 111)
s.add(p4, 135)
s.add(p5, 90)
s.add(p4, 35)
s.set_discount('Food', '25%', 'Ramen')
s.sell_product('Ramen', 15)
s.sell_product('Sub Woofer', 10)
s.set_discount('Electronic', '15%', 'Sub Woofer')
s.sell_product('Sub Woofer', 25)
s.get_all_products()
s.sell_product('Lamp', 10)
s.get_product_info('Ramen')
s.get_product_info('Lamp')
s.get_income()
