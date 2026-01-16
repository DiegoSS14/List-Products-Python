import json

class AbstractCrud:

    def detalhar(self):
        return self.__dict__
    
    def insert(self):
        list = self.find()
        list.append(self.detalhar())
        with open(self.file, 'w') as file:
            json.dump(list, file, indent=4)
        print('Item criado com sucesso!')

    def update(self, index):
        list = self.find()
        list[index] = self.detalhar()
        
        with open(self.file, 'w') as file:
            json.dump(list, file, indent=4)
        print('Item atualizado com sucesso!')

    @classmethod
    def findAll(cls):
        list = cls.find()
        for i, p in enumerate(list):
            print(f'{i} - {p}')

    @classmethod
    def find(cls, index = None):
        try:
            with open(cls.file) as file:
                list = json.load(file)
            return list[index] if isinstance(index, int) else list
        except:
            return []