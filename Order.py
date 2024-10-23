from Product import Product


class Order:
    def __init__(self):
        self.products: dict[Product, int] = {}

    def add_product(self, product: Product, quantity: int) -> None:
        """
        Добавляет товар в заказ.

        :param product: Объект товара.
        :param quantity: Количество товара для добавления.
        :raises ValueError: Если товара недостаточно на складе или quantity <= 0.
        """
        if quantity <= 0:
            raise ValueError("Количество товара должно быть положительным.")

        if product.stock < quantity:
            raise ValueError(f"Недостаточно товара {product.name} на складе. "
                             f"Доступно: {product.stock}, запрошено: {quantity}")

        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

        product.update_stock(-quantity)  # Уменьшаем количество на складе

    def calculate_total(self) -> float:
        """
        Рассчитывает общую стоимость заказа.

        :return: Общая стоимость заказа.
        """
        return sum(product.price * quantity for product, quantity in self.products.items())


def main() -> None:
    """
    Демонстрирует работу классов Product и Order,
    моделируя создание заказа и добавление товаров.
    Включает обработку ошибок, связанных с недостаточным количеством товара на складе.
    """
    product1 = Product("Телефон", 1000.0, 5)
    product2 = Product("Ноутбук", 2000.0, 3)
    order = Order()

    try:
        order.add_product(product1, 2)
        order.add_product(product2, 1)
        order.add_product(product1, 3)  # Попробуем добавить больше, чем есть на складе
    except ValueError as e:
        print(f"Ошибка при добавлении товара: {e}")

    print(f"Общая стоимость заказа: {order.calculate_total()}")


if __name__ == "__main__":
    main()
