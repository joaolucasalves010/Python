class Pessoa:
  def __init__(self, nome=None, idade=None):
    self.nome = nome
    self.idade = idade

  @classmethod
  def criar_de_data_nascimento(cls, ano, mes, dia, nome):
    idade = 2024 - ano
    return Pessoa(nome, idade)

  def maior_idade(idade):
    if idade >= 18:
      return True
    else:
      return False

p1 = Pessoa("João", 16)
print(p1.idade, p1.nome)

p2 = Pessoa.criar_de_data_nascimento(ano=2008, mes=5, dia=14, nome="Joao Lucas")
print(p2.idade, p2.nome)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))