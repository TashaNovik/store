from dask.order import order

from Order import Order

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product in self.products:
            print(f"Error: Product '{product.name}' already exists.") # Информативное сообщение
        else:
            self.products.append(product)


    def list_products(self):
        for product in self.products:
            print((f"Продукт {product.name} по цене "
            f"{product.price} в количестве {product.stock}"))

    def create_order(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name and product.quantity >= quantity:
                product.quantity -= quantity
                print(f"Order created: {quantity} x {product_name}")
                return  # Заказ создан, выходим из функции
        print(f"Error: Product '{product_name}' not found or not enough in stock.")