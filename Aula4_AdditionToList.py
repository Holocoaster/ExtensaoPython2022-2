#Import library 

import sqlite3

#Estabilish connection with the data base

connection = sqlite3.connect("dc_universe.db")

#Create a cursor type object

cursor = connection.cursor()

#Data base command // Adding The Flash into the data base, as the 12th

sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', Herói(na))"

#Execute SQL command

print(cursor.execute(sql))
#cursor.execute(sql)


#Commit the INSERT command, and close the data base

cursor.commit()
connection.close()



