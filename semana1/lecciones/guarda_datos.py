import pymongo

def main():

    connection = pymongo.MongoClient("mongodb://localhost")

    db = connection.m101
    people = db.people

    person = {'nombre':'Barack Obama', 'rol':'Presidente',
              'direccion': {'direccion1': 'La casa blanca',
                          'calle': '1600 Pennsylvania Avenue',
                          'estado' : 'DC',
                          'ciudad': 'Washington'},
              'intereses':['gobierno', 'basketball', 'comida oriental']}

    people.insert(person)


main()
