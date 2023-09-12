#Faça um programa que valide a senha de uma empresa.

import getpass

senha = getpass.getpass('Digite a senha de acesso a empresa: ')

if senha == '1234':
    print('Acesso concedido')
else:
    print('Acesso negado')