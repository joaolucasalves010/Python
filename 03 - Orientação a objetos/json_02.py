from pathlib import Path
import json

CAMINHO_DO_ARQUIVO = Path(__file__).parent / "02.json"

class Pessoa:
  def __init__(self, idade, nome):
    self.nome = nome
    self.idade = idade

bd = [] # transformando a classe em dicionário para converter em json

if __name__ == "__main__":

  def fazer_dump():
    with open(CAMINHO_DO_ARQUIVO, 'w', encoding='utf-8') as file:
      json.dump(bd, file, ensure_ascii=False, indent=2)

  while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    pessoa = Pessoa(nome=nome, idade=idade)
    opcao = input("Deseja continuar [S/N]: ")
    bd.append(pessoa.__dict__)
    if opcao.upper() == "N":
      fazer_dump()
      break
    else:
      continue


