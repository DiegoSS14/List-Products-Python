import json

class AbstractCrud:

    def detalhar(self):
        return self.__dict__
    
    def insert(self):
        list = self.find()
        list.append(self.detalhar())
        self.__saveFile(list)

    def update(self, index):
        list = self.find()
        list[index] = self.detalhar()
        self.__saveFile(list)

    @classmethod
    def delete(cls, index):
        list = cls.find()
        try:
            del list[index]
            with open(cls.file, "w") as file:
                json.dump(list, file, indent=4)
            print('Operação realizada com sucesso!')
        except:
            print("Item não encontrado!\nProvavelmente não existem mais dados...")

    def __saveFile(self, list):
        with open(self.file, 'w') as file:
            json.dump(list, file, indent=4)
        print('Operação realizada com sucesso!')

    @classmethod
    def listAll(cls):
        list = cls.find()
        for i, p in enumerate(list):
            print(f'{i + 1} - {p}')
        print()

    @classmethod
    def find(cls, index = None):
        try:
            with open(cls.file) as file:
                list = json.load(file)
            return list[index] if isinstance(index, int) else list
        except:
            return []