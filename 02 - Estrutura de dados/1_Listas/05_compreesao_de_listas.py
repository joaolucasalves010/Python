# Fitro 1
numeros = list(range(10))
pares = []

for numero in numeros:
  if numero % 2 == 0:
    pares.append(numero)

print(pares)

# Filtro 2

numeros2 = list(range(10))

numero2 = [numero for numero in numeros if numero % 2 == 0]

for i in range(len(numero2)):
  print(numero2[i])


# Filtro quadrado 1 

array = [0, 2, 4, 8, 16, 32]
quadrados = []

for quadrado in array:
  quadrados.append(quadrado ** 2)

print(quadrados)

# Filtro quadrado 2

array2 = [1, 30, 21, 2, 9, 65, 34]
quadrado2 = [quadrado ** 2 for quadrado in array2]

print(quadrado2)