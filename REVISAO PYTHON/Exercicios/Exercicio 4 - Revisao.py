#4. Faça um programa que sorteie um nome de uma lista.

import random

nomesSorteados = []

i = int (input('Digite a quantidade de nomes que serão sorteados:  '))

for _ in range(i):
    nome = input('Digite um nome: ')
    nomesSorteados.append(nome)


nomeSorteado = random.choice(nomesSorteados)
print(f'O nome sorteado é: {nomeSorteado}')