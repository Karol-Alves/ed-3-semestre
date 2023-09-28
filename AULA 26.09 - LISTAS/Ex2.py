'''Criar um programa em Python que solicite ao usuário o nomes de 5 pessoas e armazenar em uma lista.
Em seguida, o programa deve classificar os nomes de modo ascendente e solicitar ao usuário um número de 0 a 4,
correspondendo ao índice, e o programa deverá mostrar o nome armazenado nesse índice.'''

# Crie uma lista vazia para armazenar os nomes
nomes = []

# Solicite ao usuário cinco nomes
for i in range(5):
    nomeUsuario = input('Digite um nome: ')
    nomes.append(nomeUsuario)

# Classifique os nomes em ordem ascendente
nomesAscendente = sorted(nomes)

# Solicite ao usuário um número de 0 a 4
while True:
    indice = int(input('Digite um valor de 0 a 4: '))
    
    if indice >= 0 and indice < 5:
        # Exiba o nome armazenado nesse índice
        nome = nomesAscendente[indice]
        print(f'O nome armazenado no índice {indice} é: {nome}')
        break
    else:
        print('Digite um valor válido (0 a 4).')
