# os path trabalhando com caminho de diretorios 

import os
from time import sleep
from pathlib import Path

caminho = os.path.join('home', 'users', 'Desktop', 'curso', 'arquivo.txt')
print(caminho)

diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho)
print(diretorio, arquivo)
print(caminho_arquivo, extensao_arquivo)

caminho_2 = os.path.join('C:\Workspace\Python')

if os.path.exists(caminho_2):
  print(f"Caminho {caminho_2} existe")

print(os.path.abspath('.')) # temos a opção de utilizar o pathlib
print(os.path.dirname(diretorio))
print(os.path.basename(diretorio))
print(os.path.basename(caminho))
  