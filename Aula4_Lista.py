#Import library 

import sqlite3

#Estabilish connection with the data base

connection = sqlite3.connect("dc_universe.db")

#Create a cursor type object

cursor = connection.cursor()

#Data base command

sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#Execute the sql command in SQLlite in cursor

cursor.execute(sql)

#Display all names in the data base 

people = cursor.fetchall()
for person in people: 
 print (person)

for person in people:
  print(f"Nome: {person[1]}, ({person[3]})")