from classes.Product import Product
from classes.Categoria import Categoria

class Crud:

    @staticmethod
    def execute():
        operador = 1

        while operador != 0:
            Crud.printMenu(['Adicionar', 'Editar', 'ver todos',  'excluir', 'Preço quantidade total de produto'])
            print('0 - sair')
            print('===============\n')
            operador = int(input('Digite o número do que você deseja fazer: '))

            match operador:
                case 1:
                    try:
                        print()
                        id = input('Digite o id: ')
                        name = input('Digite o nome: ')
                        price = float(input('Digite o valor: '))
                        quantity = int(input('Digite o quantidade: '))
                        newProd = Product(id, name, price, quantity)
                        print()
                        newProd.insert()
                    except:
                        print('Você digitou algum valor inválido, tente novamente!')
                    print()
                case 2:
                    print()
                    try:
                        Product.listAll()
                        print()
                        index = int(input('Qual item você deseja editar? ')) - 1
                        item = Product.find(index)
                        name = input('Digite o novo nome: ')
                        price = float(input('Digite o novo valor: '))
                        quantity = int(input('Digite a nova quantidade: '))

                        updateProd = Product(item['id'], name=name, price=price, quantity=quantity)
                        updateProd.update(index)
                    except:
                        print('Você digitou algum valor inválido, tente novamente!')
                    print()
                case 3:
                    print()
                    print(Product.listAll())
                    print()
                case 4:
                    print()
                    Product.listAll()
                    index = int(input('Qual item você deseja excluir? ')) - 1
                    Product.delete(index)
                    print()
                case 5:
                    print()
                    Product.listAll()
                    index = int(input('Qual item você deseja excluir? ')) - 1
                    product = Product.find(index)
                    total = Product.getTotalPrice(product)
                    print(f'\nO valor total desse produto é R$ {total}')
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