from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent

print(ROOT_PATH)

try:
  with open(ROOT_PATH / ".txt" / "lorem.txt", "r") as arquivo:
    print("Arquivo aberto com sucesso")
except Exception as exc:
  print(f"Um erro ocorreu ao tentar abrir o arquivo {exc}")


# try:
#   with open(ROOT_PATH / ".txt" / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.write("Manipulando arquivo")
# except Exception as exc:
#   print(f"Erro ao tentar abrir o arquivo {exc}")

try:
  with open(ROOT_PATH / ".txt" / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
    print(arquivo.read())
except UnicodeDecodeError as exc:
  print(exc)
  print("Você esta tentando ler um caracter utf-8 com ASCII")