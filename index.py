from classes.Product import Product
from classes.Categoria import Categoria

produto1 = Product('001', 'Lapis')
produto2 = Product('002', 'Caneta')
categoria = Categoria('Eletronicos')

# produto1.insert()
# produto2.insert()

# categoria.insert()

# print(Product.find(3))

item = 0
findItem = Product.find(item)

produtoUpdate = Product(findItem['id'], findItem['name'], 100, 195)
produtoUpdate.update(item)