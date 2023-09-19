#Faça um programa que leia o nome e idade de uma pessoa. Determine criterios para mostrar se a pessoa é adolescente, adulto ou idoso

def classificarIdade():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    if idade < 12:
        print('Criança')
    elif 12 <= idade < 18:
        print('Adolescente')
    elif 18 <= idade <= 70:
        print('Adulto')
    else:
        print('Idoso')

classificarIdade()