import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

print(ROOT_PATH)

# os.mkdir(ROOT_PATH / 'os_shutil_teste')

# file = open(ROOT_PATH / "teste.txt", "w")
# file.close()

# os.rename(ROOT_PATH / "teste.txt", ROOT_PATH / "novo_nome.txt")

# os.remove(ROOT_PATH / "novo_nome.txt")

# shutil.move(ROOT_PATH / "novo_nome.txt", ROOT_PATH / "os_shutil_teste" / "novo_nome.txt")