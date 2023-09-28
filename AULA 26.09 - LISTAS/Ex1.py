'''Faça um programa em Python que calcule a média de um aluno a partir de cinco notas previamente armazenadas em uma lista.
Utilize: notas = [6, 7, 6.5, 4.8, 8]'''

notas = [6, 7, 6.5, 4.8, 8]

soma = sum(notas)  # Soma todas as notas da lista
quantidade = len(notas)  # Obtém o número de notas na lista
media = soma / quantidade  # Calcula a média

print(f'Sua média é {media:.2f}')