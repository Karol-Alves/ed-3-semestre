#Faça um programa que leia o nome e 3 notas do aluno, em seguida calcule sua média, se a média for maior que 6, imprima Aprovado, senão, imprima Reprovado.

def mediaSimples ():
  nome = input('Digite seu nome: ')
  n1 = float (input('Digite a nota 1: '))
  n2= float (input('Digite a nota 2: '))
  n3= float (input('Digite a nota 3: '))

  media = float(n1+n2+n3/3)

  if media >= 6:
    print('Aprovado')
  else:
    print('Reprovado')

mediaSimples()