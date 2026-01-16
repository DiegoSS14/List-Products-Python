from classes.Product import Product
from classes.Categoria import Categoria

produto1 = Product('001', 'Lapis')
produto2 = Product('002', 'Caneta')

# produto1.insert('products')
# produto2.insert('products')

categoria = Categoria('Eletronicos')
# categoria.insert('categories')

categoria.findAll('categories')
produto1.findAll('products')