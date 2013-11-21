
import pymongo
import sys

# estableciendo la coneccion en la base de datos
connection = pymongo.Connection("mongodb://localhost", safe=True)

# obtener un identificador para la base de datos de la escuela 
db=connection.school
scores = db.scores


def find():

    print "encontrar, informando para servicio"

    query = {'type':'exam', 'score':{'$gt':50, '$lt':70}}

    try:
        iter = scores.find(query)

    except:
        print "Error inesperado:", sys.exc_info()[0]

    sanity = 0
    for doc in iter:
        print doc
        sanity += 1
        if (sanity > 10):
            break
        

find()

