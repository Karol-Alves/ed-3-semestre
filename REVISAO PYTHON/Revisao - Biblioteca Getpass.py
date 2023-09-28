import getpass

senha = getpass.getpass('Informe a senha: ') #Armanezar senhas e validar

if senha == '123':
  print("Acesso liberado")
else:
  print("Acesso não liberado")
