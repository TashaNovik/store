from Order import Order
from Product import Product
from typing import List, Dict


class Store:
    def __init__(self):
        """Инициализирует пустой магазин."""
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в магазин.
        :param product: Объект товара для добавления.
        """
        if product in self.products:
            print(f"Ошибка: Товар '{product.name}' уже существует.")
        else:
            self.products.append(product)

    def list_products(self) -> list[dict]:
        """
        Отображает все товары в магазине с их ценами и количеством на складе.
        :return: Список словарей, содержащих информацию о каждом продукте.
        """
        product_info = []
        for product in self.products:
            product_info.append({
                "name": product.name,
                "price": product.price,
                "stock": product.stock
            })
            print(f"Продукт: {product.name}, Цена: {product.price}, Количество: {product.stock}")
        return product_info

    def create_order(self, items: dict[str, int]) -> Order:  # Принимаем словарь с названиями и количеством товаров
        """
        Создает новый заказ.
        :param items: Словарь, где ключи - названия товаров, а значения - количество.
        :return: Новый объект Order.
        :raises ValueError: Если товара нет в магазине или недостаточно на складе.
        """
        order = Order()
        for product_name, quantity in items.items():
            product = self._find_product(product_name)  # Вспомогательный метод для поиска продукта по имени
            if not product:
                raise ValueError(f"Товар '{product_name}' не найден в магазине.")

            if product.stock < quantity:
                raise ValueError(f"Недостаточно товара '{product_name}' на складе.")

            order.add_product(product, quantity)

        return order

    def _find_product(self, product_name: str) -> Product | None:
        """
        Вспомогательный метод для поиска продукта по имени.
        :param product_name: Название продукта.
        :return: Объект Product или None, если продукт не найден.
        """
        for product in self.products:
            if product.name == product_name:
                return product
        return None
