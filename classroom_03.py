# Завдання 2. Модифікувати клас Shop магічними методами
# Dunder method: contains str getitem

class Discount:
		def __init__(self, product, percentage):
				self.product = product
				self.percentage = percentage

class Shop:
		def __init__(self, name, address, type_, working_hours='9-20', employee_count=3):
				self.name = name
				self.address = address
				self.shop_type = type_
				self.working_hours = working_hours
				self.employee_count = employee_count
				self.discounts = {}

		def change_name(self, new_name):
				self.name = new_name

		def change_address(self, new_address):
				self.address = new_address

		def set_discount(self, product, percentage):
				discount = Discount(product, percentage)
				self.discounts[product] = discount

		def get_discount(self, product):
				if product in self.discounts:
						return self.discounts[product].percentage
				else:
						return None

		def __contains__(self, value):
				return any(getattr(self, attr, None) == value for attr in ['name', 'address', 'shop_type', 'working_hours', 'employee_count'])

		def __str__(self):
			return f"Shop: {self.name}\nAddress: {self.address}\nType: {self.shop_type}\nWorking Hours: {self.working_hours}\nEmployee Count: {self.employee_count}"

		def __getitem__(self, field):
			return getattr(self, field, None)

shop1 = Shop(name='ATB', address='Bolshaja Kolcevaja', type_='Grocery', working_hours='10-21', employee_count=7)

shop1.set_discount('Cheese', 15)
shop1.set_discount('Apple', 7)
shop1.set_discount('Banana', 10)

cheese_discount = shop1.get_discount('Cheese')
apple_discount = shop1.get_discount('Apple')
banana_discount = shop1.get_discount('Banana')

print(shop1.name)
print(f'Discount Cheese: {cheese_discount}%')
print(f'Discount Apple: {apple_discount}%')
print(f'Discount Banana: {banana_discount}%')

print(f"Check Cheese in shop1: {'Cheese' in shop1}")
print(shop1)
print(shop1['Cheese'])
