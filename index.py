from classes.Product import Product
from classes.Categoria import Categoria

class Crud:

    @staticmethod
    def execute():
        operador = 1

        while operador > 0:
            Crud.printMenu(['Adicionar', 'Editar', 'ver todos',  'excluir'])
            print()
            operador = int(input('Digite o número do que você deseja fazer: '))

            match operador:
                case 1:
                    print()
                    id = input('Digite o id: ')
                    name = input('Digite o nome: ')
                    price = float(input('Digite o valor: '))
                    quantity = int(input('Digite o quantidade: '))

                    newProd = Product(id, name, price, quantity)
                    print()
                    newProd.insert()
                    print()
                case 2:
                    print()
                    index = int(input('Digite o index: '))
                    id = input('Digite o id: ')
                    name = input('Digite o nome: ')
                    price = float(input('Digite o valor: '))
                    quantity = int(input('Digite o quantidade: '))
                    updateProd = Product(id, name, price, quantity)
                    print()
                    updateProd.update(index)
                    print()
                case 3:
                    print()
                    print(Product.find())
                    print()
                case 4:
                    print()
                    index = int(input('Digite o index do produto que deseja excluir: '))
                    Product.delete(index)
                    print()

        print('Programa finalizado... Obrigado!')

    @staticmethod
    def printMenu(menu):
            print('===============')
            count = 1
            for i in menu:
                print(f'{count} - {i}')
                count += 1

Crud.execute()