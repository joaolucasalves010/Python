class Pessoa:
  ano_atual = 2024


  def __init__(self, nome, idade):
    self.nome = nome 
    self.idade = idade

  @property
  def get_ano_nascimento(self):
    return Pessoa.ano_atual - self.idade
  
p1 = Pessoa(nome="João Lucas", idade=16)

print(p1.get_ano_nascimento)
