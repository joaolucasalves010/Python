import sqlite3
from main import DB_FILE, DB_NAME, TABLE_NAME, ROOT_DIR

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# cursor.execute(f"SELECT * FROM {TABLE_NAME}")
# for row in cursor.fetchall():
#   _id, name, weight = row
#   print(_id, name, weight)


# nome = input()
cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = ?", (3,))
user = cursor.fetchone()
print(user[0], user[1], "{:.2f}".format(user[2]))


# cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name = ?", (nome, ))
# user = cursor.fetchone()
# if user:
#   print(user)

cursor.close()
connection.close()