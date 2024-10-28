from pathlib import Path
import os

ROOTH_PATH = Path(__file__).parent

print(ROOTH_PATH)


try:
  arquivo = open(ROOTH_PATH / "novo-diretorio")
except FileNotFoundError as exec:
  print("Arquivo não encontrado")
  print(exec)
except IsADirectoryError as exec:
  print("Não foi possivel abrir o arquivo")
except IOError as exec:
  print("Erro ao abrir o arquivo")
except Exception as exec:
  print(exec)