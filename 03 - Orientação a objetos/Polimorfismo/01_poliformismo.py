class Passaro:
  def voar(self):
    print("Voando")

class Pardal(Passaro):
  def voar(self):
    super().voar()

class Galinha(Passaro):
  def voar(self):
    print("Galinha não voa!")

def plano_de_voo(passaro):
  passaro.voar()

plano_de_voo(Pardal())
plano_de_voo(Galinha())

# Exemplo peixe

class Peixe:
  def respirar_em_baixo_agua(self):
    print("Respirando em baixo da agua")

class Tucunare(Peixe):
  @property
  def respirar_em_baixo_agua(self):
    super().respirar_em_baixo_agua()

class PeixeBoi(Peixe):
  @property
  def respirar_em_baixo_agua(self):
    print("Peixe boi precisa de ar")

def respira_em_baixo_da_agua(peixe):
  peixe.respirar_em_baixo_agua

respira_em_baixo_da_agua(PeixeBoi())
respira_em_baixo_da_agua(Tucunare())
print(PeixeBoi().respirar_em_baixo_agua)
