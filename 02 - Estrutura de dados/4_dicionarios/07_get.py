contatos = {
  "example@gmail.com": {"name": "example", "telefone": "example"}
}

# contatos["chave"] KeyError, ou seja uma exceção será lançada se utilizarmos uma chave inexistente

print(contatos.get("chave")) # None
print(contatos.get("chave", {})) # {}
print(contatos.get("example@gmail.com", {})) 