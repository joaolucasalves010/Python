import pymysql
import dotenv
import os

import pymysql.cursors

TABLE_NAME = "customers" # > nome da tabela
dotenv.load_dotenv() # carregando dotenv

# CRUD - CREATE READ UPDATE DELETE

# Conectando com a data base
connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_USER_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor # Fazendo o cursor retornar em formato de dicionário
)

with connection:
    with connection.cursor() as cursor:
        # SQL para criar a tabela
        sql_table = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            idade INT NOT NULL
        )
        """
        cursor.execute(sql_table)
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}") # >> ZERA TODA NOSSA TABELA
        connection.commit()

    with connection.cursor() as cursor:
        # SQL para inserir um registro
        while True:
          nome = input("Digite seu nome: ")
          idade = int(input("Digite sua idade: "))
          data = dict(nome=nome, idade=idade) # Criando dicionário
          print(data)
          cursor.execute(f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(nome)s, %(idade)s)', data)
          # Inserindo vários valores com executemany
          data2 = (
            {"nome": "Glenda", "idade": 17},
            {"nome": "Carla", "idade": 17},
            {"nome": "Adryann", "idade": 22},
          )
          data3 = (
            ("Marcos", 16),
            ("Marcelo", 44),
            ("Franciele", 19)
          )
          cursor.executemany(f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(nome)s, %(idade)s)", data2)
          cursor.executemany(f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES(%s, %s)", data3)
          connection.commit()
          opc = input("Deseja cadastrar outro usuário novamente? S/N ")
          if opc.upper() == 'S':
            continue
          else:
            break
    
    # Realizando consulta 
    with connection.cursor() as cursor:
       opc = input("Deseja realizar alguma consulta? (S/N): ")
       if opc.upper() == "S":
          tipo_opc = input("Qual tipo de opc para consulta você quer (id, nome): ")
          if tipo_opc.lower() == "id":
            id = int(input("Digite o id aq: "))
            cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = %s", (id, ))
            user = cursor.fetchone()
            print(user["id"], user["nome"], user["idade"])
          elif tipo_opc.lower() == "nome":
            nome = input("Digite o nome do usuário aqui: ")
            cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE nome = %s", (nome.lower(), ))
            user = cursor.fetchone()
            print(user[0], user[1], user[2])
       else:
         print("Obrigado!")
    
    # Visualizando a tabela
    with connection.cursor() as cursor:
       opc = input("Deseja visualizar a tabela? (S/N): ")
       if opc.upper() == "S":
          cursor.execute(f"SELECT * FROM {TABLE_NAME}")
          table = cursor.fetchall()
          for row in table:
            print(row["id"], row["nome"], row["idade"])
       elif opc.upper() == "N":
          print("Obrigado!")
       else:
        print("Opção indisponível!")

    # Apagando com delete
    with connection.cursor() as cursor:
       opc = input("Você deseja deletar algum usuário da sua tabela? ")
       if opc.upper() == 'S':
          nome_usuario = input("Digite o usuário desejado: ")
          cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE nome = %s", (nome_usuario, ))
          connection.commit()
       else:
          print("Obrigado!")
      
    with connection.cursor() as cursor:
      opc = input("Você deseja atualizar algum usuário da sua tabela? ")
      if opc.upper() == 'S':
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        id_usuario = int(input("Digite o id do usuário: "))
        cursor.execute(f"UPDATE {TABLE_NAME} SET nome=%s, idade=%s WHERE id = %s", (nome, idade, id_usuario))
        connection.commit()
      else:
        print("Obrigado!")