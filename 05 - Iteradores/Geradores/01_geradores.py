def my_generator(numeros: list[int]):
  for numero in numeros:
    yield numero * 2

for i in my_generator(numeros=[1, 2, 3, 4]):
  print(i)