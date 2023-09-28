#REVISAO DE FOR E WHILE

for i in range (5):
  print('Aula')
print ('Python')

for i in range (1, 20 , 2):
  print(i)

cont = 0

while cont <=10:
  print('aula')
  cont +=1

while True:
    n1 = int(input('Número ou 0 para sair:  '))
    if n1==0:
        print('Fim do programa!')
    break
