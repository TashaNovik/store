from Product import Product

class Order:
    def __init__(self):
        self.products = {}  #Словарь товаров в заказе: {product: quantity}

    def add_product(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Недостаточное количество товара на складе")

        if product in self.products:
            # Если продукт уже есть в заказе, увеличиваем количество:
            self.products[product] += quantity
        else:
            #Если продукта в заказе нет, добавляем продукт в заказ:
            self.products[product] = quantity

    def calculate_total(self):
        total_price_order = 0
        for product, quantity in self.products.items():
            total_price_order = total_price_order + product.price * quantity
        return total_price_order

def main():
    product1 = Product("Телефон", 1000, 5)
    product2 = Product("Ноутбук", 2000, 3)
    order = Order()
    order.add_product(product1, 2)
    order.add_product(product2, 1)
    print(order.calculate_total())  # 4000
    order.add_product(product1, 3)  # добавили еще телефонов
    print(order.calculate_total())  # 7000

if __name__ == "__main__":
    main()