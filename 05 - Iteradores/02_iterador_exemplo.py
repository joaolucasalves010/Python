class MeuIterador:
  def __init__(self, numeros: list[int]):
    self.numeros = numeros
    self.contador = 0

  def __iter__(self):
    return self

  def __next__(self):
    try:
      numero = self.numeros[self.contador]
      self.contador += 1
      return numero * 2
    except:
      raise StopIteration

for i in MeuIterador(numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
  print(i)