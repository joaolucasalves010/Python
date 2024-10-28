def meu_decorador(funcao):
  def executar(*args, **kwargs):
    resultado = funcao(*args, **kwargs)
    return resultado

  return executar


@meu_decorador
def executar_funcao(nome):
  print(f"Ola {nome}")
  return nome.upper()

resultado = executar_funcao("João")
print(resultado)
print(executar_funcao)