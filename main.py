#Import library 

import Aula4_DBFunction as Function

connection, cursor = Function.connect()

name = input("Insert the hero's/villain's name: ")
alter_ego = input("Insert the alias: ")
numeric_type = input("Type 1 for HERO and 2 for VILLAIN: ")

#Checks the max value within the list

sql = "SELECT MAX(pessoa_id) FROM pessoas"
cursor.execute(sql)
cursor.fetchone()



