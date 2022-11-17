#Import library 

import sqlite3

#Function creation

def connect():
  
  #Estabilish connection
  connection = sqlite3.connect("dc_universe.db")

  #Cursor type object
  cursor = connection.cursor()

  return connection, cursor



