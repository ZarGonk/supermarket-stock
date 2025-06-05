# 3. Estoque de Produtos
#       Adicionar novos produtos.
#       Atualizar a quantidade de um produto.
#       Mostrar todos os produtos com seus estoques.
#       Finalizar Programa

from time import sleep
from arquiLib import *

# Passo-a-Passo

# 1. Criar um dicionario = Estoque
stock = {}

def add_product():
    name = str(input('Digite nome do Produto: ')).strip().capitalize()
    
    #Verifica se o produto esta no estoque
    if name in stock:
        print(f'Item {name}, ja foi adicionado ao estoque')
        #Se tiver entra no while
        while name in stock:
            name = str(input('\nTente outro produto: ')).strip().capitalize()
        
        amount = get_amount()
        stock[name] = amount

    else:
        amount = get_amount()
        stock[name] = amount


def att_product():
    name = str(input('Produto que deseja atualizar: ')).strip().capitalize()
    
    #Verifica se o produto não esta no estoque 
    while not name in stock:
        print(f'Item {name}, Não encontrado')
        name = str(input('\nTente outro produto: ')).strip().capitalize()

    amount = get_amount()
    stock[name] = amount
    

def show_product():
    #Imprime o cabeçalho
    print('ESTOQUE'.center(35))
    print('-' * 35)
    print('| {:^14} | {:^14} |'.format('Produtos', 'Quantia'))
    print('|' + '-' * 33 + '|')
    for item, value in stock.items():
        print(f'| {item:<14} | {value:>8}       |')
    print('-'*35)


def get_amount():
    """
    Solicita e retorna a quantidade de um produto como um número inteiro.

    Utiliza um loop para garantir que o valor inserido seja um número inteiro válido.
    - Caso o usuário insira um valor inválido (não inteiro), exibe uma mensagem de erro e solicita novamente.

    Retorna:
        int: A quantidade informada pelo usuário.

    Exemplo de uso:
        quantidade = get_amount()
    """
    while True:
        try:
            return int(input('Quantia do produto: '))
        except ValueError:
            print('Valor invalido, Somente numeros inteiros')
            continue

# 2. Criar menu de Opções
def menu():
    print('~'*40)
    print('1. Adicionar novos produtos\n2. Atualizar a quantia de um produto\n3. Mostrar estoque\n4. Sair')
    print('~'*40)

#main
while True:
    menu()
    while True:  
        try:
            option = int(input('Qual Opção deseja: '))
            if 1 <= option <= 4:   
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
            continue
        if 1 <= option <= 4:
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 4.")
    print()

    # 3. Função Add novos produtos
    if option == 1:
        add_product()

    # 4. Atualizar a Quantidade de um Produtos
    elif option == 2:
        att_product()
        
    # 5. Mostrar Produtos dos estoques
    elif option == 3:
        show_product()

    # 6. Finalizar o programa
    elif option == 4:
        print('Saindo',end='')
        for i in range(3):
            sleep(0.5)
            print('.',end='', flush=True)
        sleep(0.5)
        print('\nPrograma Encerrado')
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 4.")