class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает продукты по имени и цене, игнорируя количество на складе.
        """
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def update_stock(self, quantity: int) -> int:
        """
                Обновляет количество товара на складе.
                :param quantity: Положительное число при завозе, отрицательное при продаже.
                :raises ValueError: Если новое количество товара меньше нуля.
                :return: Новое количество товара на складе.
                """
        new_stock = self.stock + quantity
        if new_stock < 0:
            raise ValueError(f"Недостаточно товара {self.name} на складе. "
                             f"Доступно: {self.stock}, запрошено: {abs(quantity)}")
        self.stock = new_stock
        return self.stock

def main() -> None:
    """
    Демонстрирует работу с классом Product.
    """
    products = [
        Product("Telephone", 1000.0, 6),
        Product("Laptop", 15000.0, 12)
    ]
    for product in products:
        print(f"Добавлен продукт: {product.name}, цена: {product.price}, количество: {product.stock}")

    new_stock = products[0].update_stock(3)
    print(f"Новое количество {products[0].name} на складе: {new_stock}")
    try:
        new_stock = products[1].update_stock(-13)
        print(f"Новое количество {products[1].name} на складе: {new_stock}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    for product in products:
        print(f"Текущее количество {product.name} на складе: {product.stock}")

if __name__ == "__main__":
    main()
