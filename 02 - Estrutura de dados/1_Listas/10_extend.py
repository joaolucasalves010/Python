linguagens = ['csharp', 'c++']

print(linguagens)

linguagens2 = ['java', 'python']

linguagens.extend(linguagens2)

print(linguagens) # >> csharp c++ java python

linguagens.extend(['ruby', 'rust'])

print(linguagens) # >> csharp c++ java python ruby rust