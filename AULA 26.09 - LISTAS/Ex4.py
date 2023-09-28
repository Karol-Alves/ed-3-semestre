''' Faça um programa em Python que contenha 3 listas com os nomes: valores, par e ímpar. Solicite N números inteiros ao usuário e armazene-os na lista
chamada valores (utilize como critério de parada o valor digitado 999).
Após a obtenção dos dados, na lista par armazenar apenas os números pares da lista valores e na lista ímpar os números ímpares.
É obrigatório o uso de estrutura de repetição e listas. ▪ Exiba os números armazenados nas 3 listas.'''

# Crie três listas vazias para armazenar os valores, pares e ímpares
valores = []
pares = []
impares = []

# Solicite números inteiros ao usuário e armazene-os na lista "valores"
while True:
    numero = int(input('Digite um número inteiro (ou 999 para parar): '))
    if numero == 999:
        break  # Encerra o loop quando o usuário digita 999
    valores.append(numero)

# Separe os números em pares e ímpares
for numero in valores:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Exiba os números armazenados nas três listas
print('Valores digitados:', valores)
print('Números pares:', pares)
print('Números ímpares:', impares)