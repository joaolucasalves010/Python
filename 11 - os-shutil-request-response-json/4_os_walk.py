import os
from itertools import count

caminho = os.path.join('C:', '\Workspace', 'Python', 'exemplo')
counter = count()

for root, dirs, files in os.walk(caminho):
  the_counter = next(counter)
  print(f'{the_counter} Pasta atual: {root}')

  for _dir in dirs:
    print(f'{the_counter} dir: {_dir}')

  for file in files:
    print(f'{the_counter} file: {file}')