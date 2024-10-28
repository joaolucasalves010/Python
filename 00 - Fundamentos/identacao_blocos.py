def sacar(valor):
  saldo_atual = 500

  if saldo_atual >= valor:
    print('Valor sacado')
    print(f'Saldo atual {saldo_atual}')
  else:
    print('Saldo insuficiente')
    print(f'Saldo disponivel {saldo_atual}')
  print('Obrigado por ser nosso cliente, tenha um Bom Dia!')    

valor = float(input('Digite o valor desejado: '))

sacar(valor)
