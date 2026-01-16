from classes.AbstractCrud import AbstractCrud

class Categoria(AbstractCrud):

    file = 'db/categories.json'

    def __init__(self, name):
        self.name = name