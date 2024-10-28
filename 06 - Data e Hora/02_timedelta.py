# Exemplo 1 
from datetime import datetime, timedelta

d = datetime(2024, 9, 11, 18, 16)
print(d) # >> 2024-09-11 18:16:00

#######

# Adicionando 1 semana ao tempo do dia d

d = d + timedelta(weeks=1)
print(d) # >> 2024-09-18 18:16:00

# Exemplo 2

tempo_carro_pequeno = 30
tempo_carro_medio = 45 
tempo_carro_grande = 60

print("Qual é o tamanho do carro: ")
print(50 * '=')
print('P: Pequeno ')
print('M: Medio')
print('G: Grande ')
print(50 * '=')

tamanho_carro = input("")
dia_atual = datetime.now()

if tamanho_carro.upper() == 'P':
  print()
  data_estimada = dia_atual + timedelta(minutes=tempo_carro_pequeno)
  print(f"O carro chegou no dia {dia_atual} e ficara pronto {data_estimada}")
elif tamanho_carro.upper() == 'M':
  print()
  data_estimada = dia_atual + timedelta(minutes=tempo_carro_medio)
  print(f"O carro chegou no dia {dia_atual} e ficara pronto {data_estimada}")
elif tamanho_carro.upper() == 'G':
  print()
  data_estimada = dia_atual + timedelta(minutes=tempo_carro_grande)
  print(f"O carro chegou no dia {dia_atual} e ficara pronto {data_estimada}")
