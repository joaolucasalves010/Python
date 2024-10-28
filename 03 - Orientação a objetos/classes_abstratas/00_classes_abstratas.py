from abc import ABC, abstractmethod

class ControleRemoto(ABC):
  @abstractmethod
  def ligar(self):
    pass
  
  @abstractmethod
  def desligar(self):
    pass

class ControleTv(ControleRemoto):
  def ligar(self):
    print("Ligando TV!")
    print("Ligada!")

  def desligar(self):
    print("Desligando tv")
    print("Tv desligada")


controle = ControleTv()
controle.ligar()
controle.desligar()

class Animal:
  def mover(self):
    print(f"{self.__class__.__name__} se movendo")
  
  @abstractmethod
  def fazer_som(self):
    pass

  def dormir(self):
    print("Animal dormindo")

class Gato(Animal):
  def mover(self):
    super().mover()

  def dormir(self):
    super().dormir()

  def fazer_som(self):
    print("Miau")


gato = Gato()

gato.fazer_som()
gato.dormir()
gato.mover()

class ControleAr(ControleRemoto):
  def ligar(self):
    print("Ligar Ar")
    print("Ar ligado")

  def desligar(self):
    print("Desligar Ar")
    print("Ar desligado")

controle2 = ControleAr()
controle2.ligar()
controle2.desligar()