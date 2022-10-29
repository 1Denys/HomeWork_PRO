class Product:
    def __init__(self, name_of_product, price, description_of_product, size_of_product):
        self.name_of_product = name_of_product
        self.price = price
        self.description_of_product = description_of_product
        self.size_of_product = size_of_product

    def __str__(self):
        return f"name_of_product = {self.name_of_product}\n price = {self.price}\n " \
               f"description_of_product = {self.description_of_product}\n size_of_product = {self.size_of_product}\n"

class Buyer:
    def __init__(self, surname, name, phone_number):
        self.surname = surname
        self.name = name
        self. phone_number = phone_number

    def __str__(self):
        return f"surname = {self.surname}\n name = {self.name}\n phone_number = {self.phone_number}"

class Order:
    def __init__(self, buyer: Buyer):
        self.buyer = buyer
        self.products = []
        self.quantities = []

    def add_order(self, product: Product , quantity = 1):
        self.products.append(product)
        self.quantities.append(quantity)

    def costs(self):
        summa = 0
        for index, product in enumerate(self.products):
            summa += product.price * self.quantities[index]
        return summa

    def __str__(self):
        res = ''
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product.price} x {quantity} = {product.price * quantity} грн. \n'
        return f'{self.buyer}\n{res}\nTotal={self.costs()}'

pr_1 = Product('apple', 20, 'sweet', 'small')
pr_2 = Product('strawberry', 25, 'sweet', 'big')
pr_3 = Product('orange', 30, 'sour', 'medium')

buyer_1 = Buyer('Ivanov', 'Ivan', '0959595995')
buyer_2 = Buyer('Petrov', 'Ivan', '0958565958')

order_1 = Order(buyer_1)
order_1.add_order(pr_1)
order_1.add_order(pr_2, 10)

print(order_1)

