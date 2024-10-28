import functools

def meu_decorador(funcao):
  @functools.wraps(funcao)
  def envelope(*args, **kwargs):
    funcao(*args, **kwargs)

  return envelope

@meu_decorador
def ola_mundo(nome):
  print(f"Ola {nome}!")

ola_mundo("João")
print(ola_mundo.__name__)
print(ola_mundo)