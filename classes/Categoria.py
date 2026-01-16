from classes.AbstractCrud import AbstractCrud

class Categoria(AbstractCrud):
    def __init__(self, name):
        self.name = name