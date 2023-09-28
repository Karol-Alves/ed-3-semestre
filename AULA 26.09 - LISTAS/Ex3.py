# Crie uma lista vazia para armazenar os nomes
nomes = []

# Solicite ao usuário o nome de 5 pessoas e armazene na lista
for i in range(5):
    nome = input(f'Digite o nome {i+1}: ')
    nomes.append(nome)

# Exiba os nomes digitados e o tamanho da lista
print('Nomes digitados:', nomes)
print('Tamanho da lista:', len(nomes))

# Solicite ao usuário um nome para remover
nome_remover = input('Digite um nome para remover: ')

# Verifique se o nome está na lista antes de remover
if nome_remover in nomes:
    nomes.remove(nome_remover)
    print(f'{nome_remover} removido com sucesso.')
else:
    print(f'{nome_remover} não foi encontrado na lista.')

# Exiba os nomes restantes na lista e o tamanho atual
print('Nomes restantes:', nomes)
print('Tamanho da lista após a remoção:', len(nomes))