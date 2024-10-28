def greet(nome=None):

  print("Executando greet")

  if nome == None:
    return f"Olá, Bom dia"
  else:
    return f"Olá, bom dia {nome}"

def long_message(nome=None):
  print("Executando long message")

  if nome == None:
    return f"Olá, como você esta?"
  else:
    return f"Olá, {nome} como você esta?"

def executar(funcao, nome):
  print(f"Executando")
  return funcao(nome)

print(executar(long_message, "João Lucas"))