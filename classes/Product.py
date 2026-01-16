from classes.AbstractCrud import AbstractCrud

class Product(AbstractCrud):

    file = 'db/products.json'

    def __init__(self, id, name, price = 0, quantity = 0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

