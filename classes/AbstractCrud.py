import json

class AbstractCrud:

    def detalhar(self):
        return self.__dict__
    
    def insert(self, name: str):
        list = self._load(name)
        list.append(self.detalhar())
        with open(f'db/{name}.json', 'w') as file:
            json.dump(list, file, indent=4)

    def findAll(self, name):
        list = self._load(name)
        for i, p in enumerate(list):
            print(f'{i} - {p}')

    def _load(self, name):
        try:
            with open(f'db/{name}.json') as file:
                return json.load(file)
        except:
            return []