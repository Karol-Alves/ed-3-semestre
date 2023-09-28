#Faça um programa que valide a senha de uma empresa.

import getpass

while True:
    senha = getpass.getpass('Digite a senha de acesso a empresa: ')

    if senha == '1234':
        print('Acesso concedido')
        break  
    else:
        print('Senha incorreta. Tente novamente.')
