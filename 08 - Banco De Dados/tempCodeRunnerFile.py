
  for row in cursor.fetchall():
    _id, nome, peso = row
    print(_id, nome, peso)