from pathlib import Path
import json

CAMINHO_JSON = Path(__file__).parent / "aula1_json.json"

with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
  pessoa = json.load(f)
  print(pessoa)
  print(type(pessoa))
  