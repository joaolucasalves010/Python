import os
from time import sleep

caminho = os.path.join('C:', '\Workspace', 'Python')
print(caminho) # Printa caminho de diretório
sleep(2) # Adiciona um delay de 2 segundos
os.system(f'cd {caminho}') # Executa no terminal cd C:\Workspace\Python

for item in os.listdir(caminho):
  print(item) # Printando todos os dirétorios dentro do caminho

for pasta in os.listdir(caminho):
  caminho_completo = os.path.join(caminho, pasta)
  print(pasta)

  if not os.path.isdir(caminho_completo):
    continue

  for arquivo in os.listdir(caminho_completo):
    print(' ->', arquivo)