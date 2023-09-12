# Faça um programa que leia dois números e mostre qual o maior deles, o menor, ou se os números são iguais.

n1 = float (input('Digite o  número 1:  '))
n2 = float (input('Digite o número 2:  '))

if n1 > n2:
    print('O maior número é:', n1)
    print('O menor número é:', n2)
elif n2 > n1:
    print('O maior número é:', n2)
    print('O menor número é:', n1)
else:
    print('Os números são iguais')