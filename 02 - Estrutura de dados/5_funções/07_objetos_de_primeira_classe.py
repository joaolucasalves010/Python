def somar(a, b):
  return a + b

def subtrair(a, b):
  if a > b:
    return a - b
  else:
    return b - a

def multiplicar(a, b):
  return a * b

def exibir_resultado(a, b, funcao):
  resultado = funcao(a, b)
  print("O resultado da operação é {}".format(resultado))

exibir_resultado(10, 10, somar) # >> 20
exibir_resultado(10, 5, subtrair) # >> 5
exibir_resultado(10, 10, multiplicar) # >> 100