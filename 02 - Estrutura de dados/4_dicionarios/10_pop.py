contatos = {
  "example@gmail.com": {"name": "example", "telefone": "example"}
}

popped_item = contatos.pop("example@gmail.com")
print(popped_item)
print(contatos)

resultado = contatos.pop("example@gmail.com", "Valor Default") #  podemos alterar as chaves {} por um valor default

"""
Exemplo

resultado = contatos.pop("example@gmail.com", {}) O valor padrão é essa as chaves

Podemos setar qualquer valor

"""

print(resultado)