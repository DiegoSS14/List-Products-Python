from classes.AbstractCrud import AbstractCrud

class Product(AbstractCrud):

    file = 'db/products.json'

    def __init__(self, id, name, price = 0, quantity = 0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def insert(self):
        products = self.find() or []
        duplicatedProd = list(filter(lambda p: p.get('id') == self.id, products))

        if duplicatedProd:
            print('Já existe um produto com esse id!')
        else:
            super().insert()
