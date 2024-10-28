class Cachorro():
  def __init__(self, nome, cor, acordado=True):
    print("Inicializando a classe")
    self.nome = nome
    self.cor = cor
    self.acordado = acordado 

  def latir(self):
    print("Au au au")

  def __del__(self):
    print("Removendo instancia da classe")

cao_1 = Cachorro("Bruce", "Amarelo")

cao_1.latir()