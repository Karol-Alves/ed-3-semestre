while True:
  dia = int(input('Digite um número de 1 a 7 ou 0 para sair: '))

  if dia == 0:
    print('Fim de programa')
    break

  match dia:
    case 1:
      print('Domingo')
    case 2:
      print('Segunda')
    case 3:
      print('Terça')
    case 4:
      print('Quarta')
    case 5:
      print('Quinta')
    case 6:
      print('Sexta')
    case 7:
      print('Sábado')
    case default:
      print('Opção inválida')