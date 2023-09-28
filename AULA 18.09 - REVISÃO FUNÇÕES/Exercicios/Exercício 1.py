#1. Elabore um programa que leia dois numeros e imprima o maior, utilizando função.

def encontrarMaiorNumero():
    n1 = float(input('Digite o número 1: '))
    n2 = float(input('Digite o número 2: '))

    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return None  # Retorna None se os números forem iguais

def main():
    maior_numero = encontrarMaiorNumero()
    if maior_numero is not None:
        print(f'O maior número é: {maior_numero}')
    else:
        print('Os números são iguais.')

main()