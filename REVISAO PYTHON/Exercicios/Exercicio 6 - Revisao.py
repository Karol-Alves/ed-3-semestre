'''Faça um programa que leia o código, descrição e valor de um produto. No
final, deve mostrar os dados lidos, e o valor com 10% de desconto. O
código do produto deverá ser gerado aleatoriamente.'''

import random

codigoDoProduto = random.randint(1, 1000)

descricao = (input('Digite o nome do produto: '))

valor = float(input('Digite o valor do produto: '))

print(f'O código do produto é {codigoDoProduto}; \nO nome do produto é {descricao} \nO valor do produto é R${valor:.2f}')

valorComDesconto = valor * 0.9

print(f'O valor com 10% de desconto é R${valorComDesconto}')