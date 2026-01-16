import json

class Categoria:
    def __init__(self, name):
        self.name = name

    def detalhar(self):
        return self.__dict__
    
    def insert(self):
        try:
            with open('db/categorias.json') as file:
                list = json.load(file)
        except:
            list = []
        
        list.append(self.detalhar())
        with open('db/categorias.json', 'w') as file:
            json.dump(list, file, indent=4)