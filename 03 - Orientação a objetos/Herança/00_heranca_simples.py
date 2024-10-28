class Veiculo:
  def __init__(self, cor, placa, n_rodas):
    self.cor = cor 
    self.placa = placa
    self.n_rodas = n_rodas

  def ligar_motor(self):
    print("Ligando motor")

  def __str__(self):
    return f"Cor: {self.cor}, Numero de rodas: {self.n_rodas}, Placa: {self.placa}"

  def buzinar(self):
    print("BiBiBi")

class Carro(Veiculo):
  pass

class Caminhao(Veiculo):
  def __init__(self, cor, placa, n_rodas, carregado):
    super().__init__(cor, placa, n_rodas)
    self.carregado = carregado
    
  def esta_carregado(self):
    print(f"Sim" if self.carregado else "Não estou carregado") 

  def buzinar(self):
    super().buzinar()
    print("bamBamBam") 

class Motocicleta(Veiculo):
  pass


moto = Motocicleta("Vermelha", "NZQ3048", 2)
moto.ligar_motor()
print(moto)
caminhao = Caminhao("Preto", 'AQD1023', 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
caminhao.buzinar()
print(caminhao)