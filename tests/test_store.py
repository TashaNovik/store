import unittest
from Product import Product
from Store import Store
from Order import Order


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.product1 = Product("Test Product 1", 10.0, 5)
        self.product2 = Product("Test Product 2", 20.0, 3)

    def test_add_product(self):
        self.store.add_product(self.product1)
        self.assertIn(self.product1, self.store.products)

    def test_add_existing_product(self):
        self.store.add_product(self.product1)
        self.store.add_product(self.product1)  # Добавляем тот же товар еще раз
        self.assertEqual(len(self.store.products), 1)  # Количество товаров в магазине не должно измениться

    def test_list_products(self):
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)
        products_info = self.store.list_products()
        expected_info = [
            {'name': 'Test Product 1', 'price': 10.0, 'stock': 5},
            {'name': 'Test Product 2', 'price': 20.0, 'stock': 3}
        ]
        self.assertEqual(products_info, expected_info)

    def test_create_order(self):
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)
        order = self.store.create_order({"Test Product 1": 2, "Test Product 2": 1})
        self.assertIsInstance(order, Order) # проверяем, что order - это объект класса Order
        self.assertEqual(order.products[self.product1], 2)
        self.assertEqual(order.products[self.product2], 1)

    def test_create_order_not_enough_stock(self):
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)
        with self.assertRaisesRegex(ValueError, "Недостаточно товара"):
            self.store.create_order({"Test Product 1": 6, "Test Product 2": 1})

    def test_create_order_product_not_found(self):
        with self.assertRaisesRegex(ValueError, "не найден в магазине"):
            self.store.create_order({"Test Product 3": 1})