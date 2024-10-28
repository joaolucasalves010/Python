import json
from pathlib import Path

CAMINHO_DO_ARQUIVO = Path(__file__).parent / "aula1_json.json"

pessoa = {
  'nome': "João Lucas",
  "sobrenome": "Lima Alves",
  "endereco": [
    {'rua': 'r1', "numero": 1},
    {'rua': 'r2', "numero": 2}
  ],
  "altura": 1.83,
  "numeros_preferidos": (7, 13, 14, 77),
  "dev": True,
  "nada": None,
}

with open(CAMINHO_DO_ARQUIVO, 'w', encoding='utf-8') as file:
  json.dump(pessoa, file, ensure_ascii=False, indent=2)


# dumps: faz o dump em uma string pra utilizarmos dentro do código
# dump: faz o dump em um arquivo