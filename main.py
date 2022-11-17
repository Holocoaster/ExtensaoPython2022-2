#Import library 

import Aula4_DBFunction as Function

connection, cursor = Function.connect()

name = input("Insert the hero's/villain's name: ")
alter_ego = input("Insert the alias: ")
numeric_type = input("Type 1 for HERO and 2 for VILLAIN: ")

#Checks the max value within the list

sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cursor.execute(sql)
cursor.fetchone()

pessoa_id = cursor.fetchone()[0]

#Convertion from number keys in line 9

if numeric_type == "1":
  type = "HERO"

else:
  type = "VILLAIN"

sql =f"INSERT INTO pessoas (pessoa_id), nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil', '{tipo}')"

cursor.execute(sql)
connection.commit()
connection.close()