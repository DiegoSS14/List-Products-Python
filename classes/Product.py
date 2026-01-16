import json

class Product:
    def __init__(self, id, name, price = 0, quantity = 0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def detalhar(self):
        return self.__dict__
        # return {
        #     "id": self.id,
        #     "name": self.name,
        #     "price": self.price,
        #     "quantity": self.quantity,
        # }
    


    def insert(self):
        try:
            with open('db/products.json') as file:
                list = json.load(file)
        except:
            list = []
        
        list.append(self.detalhar())
        with open('db/products.json', 'w') as file:
            json.dump(list, file, indent=4)

