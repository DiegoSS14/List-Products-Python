from classes.Product import Product
from classes.Categoria import Categoria

class Crud:

    @staticmethod
    def execute():
        operador = 1

        while operador != 5:
            Crud.printMenu(['Adicionar', 'Editar', 'ver todos',  'excluir', 'sair'])
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
                    Product.listAll()
                    print()
                    index = int(input('Qual item você deseja editar?')) - 1
                    item = Product.find(index)

                    name = input('Digite o novo nome: ')
                    price = float(input('Digite o novo valor: '))
                    quantity = int(input('Digite a nova quantidade: '))

                    updateProd = Product(item['id'], name=name, price=price, quantity=quantity)
                    updateProd.update(index)

                    print()
                case 3:
                    print()
                    print(Product.listAll())
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
            print('===============')

Crud.execute()