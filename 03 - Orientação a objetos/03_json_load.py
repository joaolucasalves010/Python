import json
from pathlib import Path
from json_02 import Pessoa

CAMINHO_DO_ARQUIVO = Path(__file__).parent / "02.json"

bd = []

with open(CAMINHO_DO_ARQUIVO, "r", encoding="utf-8") as file:
  pessoa = json.load(file)
  for i in range(len(pessoa)):
    p = Pessoa(**pessoa[i])
    bd.append(p)

for i in range(len(bd)):
  print(f"Nome: {bd[i].nome}, Idade: {bd[i].idade}")