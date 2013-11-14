import bottle
import pymongo

# este es el encabezado por default direccion del servicio web

@bottle.route('/')
def index():
    
    # coneccion de mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # adjuntamos la base de datos test 
    db = connection.test

# obtener el identificador para la recoleccion de nombres 

    name = db.users

    # encontrar un solo documento
    item = name.find_one()

    return "<b>Hola %s </b>" % item['name']


bottle.run(host='localhost', port=8082)
