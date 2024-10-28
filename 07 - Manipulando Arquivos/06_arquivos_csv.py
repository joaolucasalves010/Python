import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent

try:
  with open(ROOT_PATH / ".txt" / "usuarios.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'Nome'])
    writer.writerow(['1', 'João Lucas'])
    writer.writerow(['2', 'Marcos'])
except Exception as exc:
  print(f"Ocorreu um erro {exc}")

try:
   with open(ROOT_PATH / ".txt" / "usuarios.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
      print(row)
except Exception as exc:
  print(f"Ocorreu um erro {exc}")