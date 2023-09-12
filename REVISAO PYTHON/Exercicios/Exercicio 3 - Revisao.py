'''Faça um programa que mostre o valor a ser pago de uma prestação. O
programa deverá ler o valor da prestação e o número de dias em atraso. Se a
prestação estiver atrasada, deverá ser aplicada uma multa de 8% + 0.03 por
dia de atraso, em seguida, mostrar o valor final. Se não, mostrar o valor
normal, sem acréscimos.'''

valorPrestacao = float(input('Digite o valor da prestação:  '))
diasDeAtraso = int (input('Digite os dias de atraso:  '))

if diasDeAtraso >= 1:
    valorAcrecido = valorPrestacao * 1.08 + diasDeAtraso * 0.03
    print(f'O valor da prestação atrasada é R${valorAcrecido:.2f}')
else:
    print(f'A prestação não está atrasada, o valor é R$ {valorPrestacao:.2f}')
