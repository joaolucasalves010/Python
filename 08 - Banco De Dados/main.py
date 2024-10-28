import sqlite3
from pathlib import Path 

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR /  DB_NAME
TABLE_NAME = "customers"

if __name__ == "__main__":
  connection = sqlite3.connect(DB_FILE)
  cursor = connection.cursor()

  # CRUD - CREATE READ UPDATE DELETE
  # SQL - INSERT SELECT UPDATE DELETE

  # CUIDADO FAZER DELETE SEM WHERE, isso exclui tudo da sua tabela
  # cursor.execute(f"DELETE FROM {TABLE_NAME}")

  cursor.execute(f"""
  CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    weight REAL
  )
  """
  )

  # Registrar valores nas colunas da tabela
  registrar_valores = (
    f"INSERT INTO {TABLE_NAME}"
    "(name, weight)"
    "VALUES (:nome, :peso)" 
  )

  # DELETE QUE DELETA TODOS OS DADOS
  cursor.execute(f"DELETE FROM {TABLE_NAME}")

  # DELETE PARA DELETAR SEQUENCIA DOS IDS
  cursor.execute(f"DELETE FROM sqlite_sequence WHERE name = '{TABLE_NAME}'")

  # DELETE MAIS CUIDADOSO
  # cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (3, )) 


  # EXEMPLO DE EXECUTE MANY
  # users = [["Marcos", 67], ["Miguel", 56]]
  # cursor.executemany(registrar_valores, users)

  dict_users = (
    {"nome": "Maria", "peso": 57},
    {"nome": "Glenda", "peso": 53},
    {"nome": "Carla", "peso": 65}
  ) 

  cursor.executemany(registrar_valores, dict_users)

  cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET weight = 56 '
    'WHERE id = 2'
  )

  cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET weight = 60 '
    'WHERE name = "Carla"'
  )

  cursor.execute(f"SELECT * FROM {TABLE_NAME}")
  for row in cursor.fetchall():
    _id, nome, peso = row
    print(_id, nome, peso)

  connection.commit()
  print(registrar_valores)


  # Fechando conexões
  cursor.close()
  connection.close()