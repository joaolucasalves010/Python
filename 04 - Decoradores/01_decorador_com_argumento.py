def meu_decorador(funcao):
  def argumentos(*args, **kwargs):
    funcao(*args, **kwargs)

  return argumentos

@meu_decorador
def executar_decorador(*args, **kwargs):
  for arg in args:
    print(arg, end="\n")

executar_decorador("Python", "Java", "C", "CPP")