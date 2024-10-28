def criar_carro(modelo, ano, placa, /, *, motor, combustivel, marca):
  print(modelo, ano, placa, motor, combustivel, marca)


criar_carro("Palio", 1999, "ABC-1234", combustivel="Gasolina", marca="Fiat", motor=1.0) # Válido
criar_carro(modelo="Palio", combustivel="Gasolina", marca="Fiat", motor=1.0) # Inválido