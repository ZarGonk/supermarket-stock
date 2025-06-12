from arquiLib import *

stock = 'stock.txt'


with open(stock, 'r', encoding='utf-8') as st:
    dados = st.readlines()


#print(dados)
for itens in dados:
    # print(itens.strip().split(',')[1])
    if 'Banana' in itens:
        print('achei')