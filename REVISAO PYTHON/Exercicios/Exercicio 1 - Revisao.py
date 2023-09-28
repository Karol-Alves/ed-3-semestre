#Exercicios

#Fazer um programa que solicite 2 números e informe:

#a) A soma dos numeros;

#B) A soma do primeiro número pelo quadrado do segundo;

#C) O quadrado do primeiro número;

#D) A raiz quadrada da soma dos quadrados;

import math

n1=int(input('Informe o número 1: '))
n2=int (input('Informe o número 2: '))

soma = n1+n2
print (f'A soma dos numeros: {soma}')

b = (math.sqrt(n2))+ n1
print(f'A soma do primeiro número pelo quadrado do segundo: {b}')

c = (math.sqrt(n1))
print(f'O quadrado do primeiro número: {c}')

quadrados = (math.sqrt(n1)) + (math.sqrt(n2))
somaRaizQuadrada = (math.sqrt(quadrados))
print(f'A raiz quadrada da soma dos quadrados: {somaRaizQuadrada}')
