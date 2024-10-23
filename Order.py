from Product import Product


class Order:
    def __init__(self):
        """Инициализирует пустой заказ."""
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

    def remove_product(self, product: Product, quantity: int) -> None:
        """
        Удаляет указанное количество товара из заказа.
        :param product: Объект товара для удаления.
        :param quantity: Количество товара для удаления.
        :raises ValueError: Если товара нет в заказе, quantity <=0, или если quantity больше, чем количество товара в заказе.
        """

        if quantity <= 0:
            raise ValueError("Количество товара для удаления должно быть положительным.")

        if product not in self.products:
            raise ValueError(f"Товар '{product.name}' не найден в заказе.")

        if self.products[product] < quantity:
            raise ValueError(f"В заказе меньше товара '{product.name}', чем запрошено для удаления. "
                             f"В заказе: {self.products[product]}, запрошено: {quantity}")

        self.products[product] -= quantity
        product.update_stock(quantity)  # Возвращаем товар на склад

        if self.products[product] == 0:
            del self.products[product]  # Удаляем товар из заказа, если количество стало 0


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
        order.add_product(product1, 3)
        order.remove_product(product1, 1)  # удаление товара из заказа
        order.add_product(product2, 1)
        order.remove_product(product1, 2)  # удаление товара из заказа
        order.remove_product(product1, 1)  # попытка удалить больше чем есть в заказе
    except ValueError as e:
        print(f"Ошибка: {e}")

    print(f"Общая стоимость заказа: {order.calculate_total()}")

    print("Товары в заказе:")
    for product, quantity in order.products.items():
        print(f"- {product.name}: {quantity}")


if __name__ == "__main__":
    main()
