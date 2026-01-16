import json

class AbstractCrud:

    def detalhar(self):
        return self.__dict__
    
    def insert(self):
        list = self._load()
        list.append(self.detalhar())
        with open(self.file, 'w') as file:
            json.dump(list, file, indent=4)

    @classmethod
    def findAll(cls):
        list = cls._load()
        for i, p in enumerate(list):
            print(f'{i} - {p}')

    @classmethod
    def _load(cls):
        try:
            with open(cls.file) as file:
                return json.load(file)
        except:
            return []