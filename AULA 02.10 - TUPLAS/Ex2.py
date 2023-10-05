import random

filaDeSenhas = []

while True:
    print('\nMenu:\n1. Gerar senha\n2. Mostrar fila de senha\n3. Chamar próxima senha\n4. Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        senha = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + ''.join(random.choices('0123456789', k=3))
        filaDeSenhas.append(senha)
        print(f'Senha gerada: {senha}')
    elif opcao == '2':
        print('Fila de senhas:')
        print('\n'.join(filaDeSenhas))
    elif opcao == '3':
        if filaDeSenhas:
            senhaChamada = filaDeSenhas.pop(0)
            print(f'Senha chamada: {senhaChamada}')
        else:
            print('A fila está vazia.')
    elif opcao == '4':
        print('Saindo do programa.')
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')
