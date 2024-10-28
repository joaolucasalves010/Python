frutas = (
  "laranja",
  "maça",
  "pera",
)

print(frutas)

letras = tuple('Python')
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ('Brasil',)
print(pais)

for i, fruta in enumerate(frutas):
  print(f'{fruta} no indice {i}')
