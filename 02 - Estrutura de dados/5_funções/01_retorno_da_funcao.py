def calcular_total(arr):
  result = 0
  for numero in arr:
    result = result + numero
  return result

def calcular_total_sum(arr):
  return sum(arr)

def return_antecessor_e_sucessor(numero):
  antecessor = numero - 1
  sucessor = numero + 1
  return antecessor, sucessor



print(calcular_total([10, 20, 34]))
print(calcular_total_sum([10, 20, 34]))
print(return_antecessor_e_sucessor(10))