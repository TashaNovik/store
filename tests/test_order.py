import unittest
from Product import Product
from Order import Order


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Test Product 1", 10.0, 5)
        self.product2 = Product("Test Product 2", 20.0, 3)
        self.order = Order()

    def test_add_product(self):
        self.order.add_product(self.product1, 2)
        self.assertEqual(self.order.products[self.product1], 2)
        self.assertEqual(self.product1.stock, 3)  # Проверяем, что количество на складе уменьшилось

    def test_add_existing_product(self):
        self.order.add_product(self.product1, 2)
        self.order.add_product(self.product1, 3)  # Добавляем тот же товар
        self.assertEqual(self.order.products[self.product1], 5)
        self.assertEqual(self.product1.stock, 0)  # Проверяем, что количество на складе уменьшилось

    def test_add_product_not_enough_stock(self):
        with self.assertRaisesRegex(ValueError, "Недостаточно товара"):
            self.order.add_product(self.product1, 6)

    def test_calculate_total(self):
        self.order.add_product(self.product1, 2)
        self.order.add_product(self.product2, 1)
        total = self.order.calculate_total()
        self.assertEqual(total, 40.0)

    def test_remove_product(self):
        self.order.add_product(self.product1, 3)
        self.order.remove_product(self.product1, 2)
        self.assertEqual(self.order.products[self.product1], 1)
        self.assertEqual(self.product1.stock, 4)  # Проверяем, что количество на складе увеличилось

    def test_remove_all_products_of_one_type(self): # Новый тест!
        self.order.add_product(self.product1, 3)
        self.order.remove_product(self.product1, 3)
        self.assertNotIn(self.product1, self.order.products)  # Проверяем, что продукт удален из заказа
        self.assertEqual(self.product1.stock, 5)  # Проверяем, что количество на складе увеличилось


    def test_remove_not_exist_product(self):
        with self.assertRaisesRegex(ValueError, "не найден в заказе"):
            self.order.remove_product(self.product1, 2)

    def test_remove_product_not_enough(self):
        self.order.add_product(self.product1, 3)
        with self.assertRaisesRegex(ValueError, "В заказе меньше"):
            self.order.remove_product(self.product1, 4)

    def test_return_product(self):
        self.order.add_product(self.product1, 3)
        self.order.return_product(self.product1, 2)
        self.assertEqual(self.order.products[self.product1], 1)
        self.assertEqual(self.product1.stock, 4)  # 2 возвращенных + 2 оставшихся = 4

    def test_return_all_products_of_one_type(self): # Новый тест!
        self.order.add_product(self.product1, 3)
        self.order.return_product(self.product1, 3)
        self.assertNotIn(self.product1, self.order.products)
        self.assertEqual(self.product1.stock, 5)  # 2 возвращенных + 2 оставшихся = 4

    def test_return_not_exist_product(self):
        with self.assertRaisesRegex(ValueError, "не найден в заказе"):
            self.order.return_product(self.product1, 2)

    def test_return_product_not_enough(self):
        self.order.add_product(self.product1, 3)
        with self.assertRaisesRegex(ValueError, "В заказе меньше"):
            self.order.return_product(self.product1, 4)