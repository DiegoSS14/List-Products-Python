from classes.Product import Product
from classes.Categoria import Categoria

produto1 = Product('001', 'Lapis')
produto2 = Product('002', 'Caneta')
categoria = Categoria('Eletronicos')

# produto1.insert()
# produto2.insert()

# categoria.insert()

Product.findAll()