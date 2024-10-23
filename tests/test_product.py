import unittest
from Product import Product


class TestProduct(unittest.TestCase):
    def test_update_stock_positive(self):
        product = Product("Test Product", 10.0, 5)
        new_stock = product.update_stock(3)
        self.assertEqual(new_stock, 8)
        self.assertEqual(product.stock, 8)

    def test_update_stock_negative(self):
        product = Product("Test Product", 10.0, 5)
        new_stock = product.update_stock(-2)
        self.assertEqual(new_stock, 3)
        self.assertEqual(product.stock, 3)

    def test_update_stock_zero(self):
        product = Product("Test Product", 10.0, 5)
        new_stock = product.update_stock(0)
        self.assertEqual(new_stock, 5)
        self.assertEqual(product.stock, 5)

    def test_update_stock_not_enough(self):
        product = Product("Test Product", 10.0, 5)
        with self.assertRaisesRegex(ValueError, "Недостаточно товара"):
            product.update_stock(-6)