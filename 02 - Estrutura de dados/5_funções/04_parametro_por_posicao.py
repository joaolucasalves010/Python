def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
  print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Toro", 2023, "NZQ-3024", marca="Fiat", motor=1.0, combustivel="Gasolina") # >> Válido pois os parâmetros foram definidos conforme os parênteses

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Inválido