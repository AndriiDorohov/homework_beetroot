from unittest import TestCase
from task03 import ProductStore, Product

class TestProductStore(TestCase):
		def setUp(self) -> None:
				self.product_store = ProductStore()
				self.amount = 10
				self.start_prod_price = 100
				self.prod = Product('Sport', 'Football T-Shirt', self.start_prod_price)
				self.prod1 = Product('Food', 'Ramen', 1.5)
				self.prod2 = Product('Food', 'Bread', 4)
				self.prod3 = Product('Sport', 'Treadmill', 5000)

		def test_add(self):
				self.product_store.add(self.prod, self.amount)
				prod_amount = self.product_store.products[self.prod]
				self.assertEqual(prod_amount, self.amount, f'Product amount is {prod_amount}, must be {self.amount}')
				self.assertEqual(self.prod.price, self.start_prod_price * 1.3)

		def test_set_discount__success(self):
				self.product_store.add(self.prod1, self.amount)
				before_dis = self.prod1.price
				self.product_store.set_discount('Ramen', 5)
				self.assertEqual(self.prod1.price, before_dis * 0.95, f'Prise is {self.prod1.price}, must be {before_dis}')

		def test_set_discount__fail(self):
				before_dis = self.prod1.price
				self.product_store.set_discount('Ramen', 5)
				self.assertEqual(self.prod1.price, before_dis, f'Prise is {self.prod1.price}, must be {before_dis}')

		def test_sell_product(self):
				self.product_store.add(self.prod2, self.amount)
				self.product_store.sell_product('Bread', 3)
				self.assertEqual(self.product_store.products[self.prod2], self.amount - 3)
				self.assertEqual(self.product_store.cash, self.prod2.price * 3)
				with self.assertRaises(Exception):
						self.product_store.sell_product('Bread', 8)

		def test_get_income(self):
				self.assertEqual(self.product_store.get_income(), 0)
				self.product_store.add(self.prod3, self.amount)
				self.product_store.sell_product('Treadmill', 3)
				self.assertEqual(self.product_store.get_income(), self.prod3.price * 3)

		def test_get_all_products(self):
				product_list = [self.prod, self.prod1, self.prod2, self.prod3]
				for product in product_list:
						self.product_store.add(product, self.amount)
				new_prod_list = self.product_store.get_all_products()
				self.assertEqual(len(new_prod_list), len(product_list))
				self.assertIn(self.prod1, new_prod_list)
				self.assertEqual(new_prod_list, self.product_store.products)

		def test_get_product_info(self):
				self.product_store.add(self.prod, self.amount)
				self.assertEqual(self.product_store.get_product_info(self.prod.name), (self.prod, self.amount))
