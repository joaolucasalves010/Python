class Bicicleta():

  def __init__(self, *, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor

  def buzinar(self):
    print("Plim Plim Plim")

  def correr(self):
    print("Correndo")

  def parar(self):
    print("Parando")

  def __str__(self):
    return f"{self.cor}, {self.modelo}, {self.ano}, {self.valor}"


viking = Bicicleta(cor="Verde", modelo="Viking", ano=2020, valor=3000)
viking.buzinar()
viking.correr()
viking.parar()

print(viking.cor)

b2 = Bicicleta(cor="Preta", modelo="Monark", ano=2000, valor=500)
print(b2)
