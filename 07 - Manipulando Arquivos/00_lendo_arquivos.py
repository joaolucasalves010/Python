file = open("lorem.txt", "r")
print(file.read()) # >> Retorna todo o texto de uma vez

print(file.readline()) # >> Lê linha a linha do arquivo

print(file.readlines()) # >> Retorna o texto de todo o arquivo em uma lista

file.close()