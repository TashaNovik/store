class Product:

    def __init__(self, name: str, price: float, stock: int ):
        self.name = name
        self.price = price
        self.stock = stock

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name

    def update_stock(self, quantity: int):
        """
        Обновляет количество товаров на складе. Товар может быть продан, а может быть добавлен на склад.
        :param quantity: Может быть положительным числом при завозе товара на склад
        и отрицательным числом при продаже товара со склада
        """
        try:
            new_stock = self.stock + quantity
            if new_stock < 0:
                raise ValueError(f"Недостаточно товара {self.name} на складе. "
                                 f"Доступно: {self.stock}, запрошено: {abs(quantity)}")
            self.stock = new_stock
            print(f"Количество товара {self.name} на складе: {self.stock}")
        except ValueError as e:
            print(f"Ошибка обновления склада: {e}")

    # Пример использования:

def main():
    product = Product("Telephone", 1000.0, 6)
    print(f"Продукт {product.name} по цене "
            f"{product.price} за единицу товара добавлен на склад в количестве {product.stock}")
    product_1 = Product("Laptop", 15000.0, 12)
    print(f"Продукт {product_1.name} по цене "
              f"{product_1.price} за единицу товара добавлен на склад в количестве {product_1.stock}")
    try:
        product.update_stock(3) #Добавить на склад 3 телефона
        product_1.update_stock(-13) #Продать со склада 3 ноутбука
    except ValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print(f"На складе доступно {product.stock} единиц продукта {product.name} ")
        print(f"На складе доступно {product_1.stock} единиц продукта {product_1.name} ")

if __name__ == "__main__":
    main()









