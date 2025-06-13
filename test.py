from arquiLib import *

stock = 'stock.txt'


with open(stock, 'r', encoding='utf-8') as st:
    dados = st.readlines()

encontre = str(input('Nome: ')).strip().capitalize()

#print(dados)
for itens in dados:
    # print(itens.strip().split(',')[1])
    if encontre in itens:
        while encontre in itens:
            encontre = str(input('\nTente outro produto: ')).strip().capitalize()
print('fim')