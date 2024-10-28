class Veiculo:
  def __init__(self, n_rodas, placa, cor):
    self.n_rodas = n_rodas
    self.placa = placa
    self.cor = cor

  def __str__(self):
    return f"{self.n_rodas}, {self.placa}, {self.cor}"

class Automovel(Veiculo):
  def __init__(self, tipo_combustivel, **kwargs):
    self.tipo_combustivel = tipo_combustivel
    super().__init__(**kwargs)

  def __str__(self):
    exibir_veiculo = super().__str__()
    return f"{exibir_veiculo}, {self.tipo_combustivel}"


class Motocicleta(Veiculo):
  def __init__(self, bateria, **kwargs):
    super().__init__(**kwargs)
    self.bateria = bateria

  def verificar_bateria(self):
    if self.bateria == True:
      print("Bateria carregada")
    else:
      print("Bateria descarregada")


moto = Motocicleta(n_rodas=2, placa="NZQ-3318", cor="Vermelha", bateria=True)
carro = Automovel(n_rodas=4, tipo_combustivel="Gasolina", placa="OES-3928", cor="Preto")

print(moto)
print(carro)

