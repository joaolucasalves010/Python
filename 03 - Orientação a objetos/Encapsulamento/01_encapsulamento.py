class Conta:
  def __init__(self, nro_agencia, saldo=0):
    self._saldo = saldo
    self.nro_agencia = nro_agencia

  def depositar(self, valor):
    self._saldo += valor

  def sacar(self, valor):
    self._saldo -= valor

  def exibir_saldo(self):
    print(self._saldo)


conta = Conta("0001", 100)

# print(conta._saldo) de acordo com o encapsulamento isso é errado, temos que utilizar o método exibir_saldo

conta.depositar(100)
conta.exibir_saldo()

print(conta.nro_agencia)