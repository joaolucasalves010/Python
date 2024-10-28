def exibir_texto():
  print("Hello World!")

def exibir_saudacao(nome = None):
  if nome == None:
    print("Ola, seja bem-vindo!")
  else:
    print(f"Olá {nome}, seja bem-vindo!")

def exibir_saudacao_2():
  print(f"Olá {nome}, seja bem-vindo")

exibir_texto()
exibir_saudacao()
exibir_saudacao("João Lucas")
exibir_saudacao_2("Guilherme")

# None == Null e Undefined em js