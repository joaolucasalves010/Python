def pai():
  print('Escrevendo da função pai')

  def filho1():
    print('Escrevendo da filho1() função')

  def filho2():
    print('Escrevendo da filho2() função')

  filho2()
  filho1()

pai()

# Outro exemplo

def calcular(operacao):
  somar = lambda a,b : a + b
  
  def subtrair(a, b):
    if a < b:
      return b - a
    else:
      return a - b
    
  if operacao == "+":
    return somar
  elif operacao == "-":
    return subtrair

resultado = calcular("+")(1, 3)
print(resultado)
resultado = calcular("-")(1, 3)
print(resultado)
