class Estudante:
  escola = "DIO"
  
  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula

  def __str__(self):  
    return f"{self.nome}, {self.matricula}, {self.escola}"
  
def mostrar_valores(*args):
  for arg in args:
    print(arg)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovana", 2)

# print(aluno_1)
# print(aluno_2)

mostrar_valores(aluno_1, aluno_2)

aluno_1.matricula = 3

print(aluno_1)