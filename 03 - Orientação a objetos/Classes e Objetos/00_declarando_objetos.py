class Cachorro:
  def __init__(self, nome, cor, acordado=True):
    self.nome = nome
    self.cor = cor
    self.acordado = acordado

  def latir(self):
    print("Auauaua")

  def dormir(self):
    self.acordado = False
    print(f"ZZZZZZ")
  
  def exibir(self):
    print(self.nome, self.cor)
  
     

cao_1 = Cachorro("Chappie", "Amarelo", False)
cao_2 = Cachorro("Bruce", "Caramelo")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)

cao_1.exibir()