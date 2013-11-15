import pymongo
from pymongo import MongoClient


#conectando la base de datos 
connection = MongoClient('localhost', 27017)

# encabezado de la coleccion de nombres

db = connection.names

names = db.names

item = names.find_one()

print item['name']

