
tes - Semana 2

## CRUD y el Mongo Shell
- Este es javascript
- BSON
    - Un superconjunto de JSON
    - Tipos
- `insert`
- `find`, `findOne`
- operadores de consultas
- consultas con notacion de puntos
    - `db.users.find({ "email.work": "foo" })`
    - `              that----^
- cursores
    - `next()`, `hasNext()`
    - `while(cur.hasNext()) printjson(cur.next())`
    - se puede modificar el cursor hasta el punto que se inicia la recuperacion de documentos , por ejemplo. `.limit(5)`, `.sort({name:-1})`, `.limit(5)`, `.skip(5)`
        - estos metodos afectan a la consulta que hizo para el PP por lo que no se puede utilizar despues de la consulta a sido enviada
        - estos se procesan en el servidor, no en el cliente
    - prevenir shell de enumerar cursor en la declaracion, anadiendo `null`: `var c = db.users.find(); null;`
- `update`    
    - sustituir el documento
    - `$set` fields
    - `$unset` fields
    - `$inc{ field: increment_amount }`
    - arrays: 
        - `$set`: valor de actualizacion en un array: `$set: { "a.2": 5 }` sets the third value in the array `a` to 5
        - `$pop`: quitar del final de la matriz (1) o el comienzo de la matriz (-1): `$pop: { a: 1 }`
        - `$push`: anadir al final del array
        - `$pushAll: { a: [1,2,3] }`: add all elements to array
        - `$pull: { a: 5 }`: remove any item by value
        - `$pullAll: { a: [1,2,3] }`: remove all items by value
        - `$addToSet: { a : 5 }`: pushes item if it doesn't exist
- upserts with `.update({},{},{ upsert: true })` 
- multi-update with `.update({},{}.{ multi: true })` (without `{multi:true}` an `update` affects only a single document)
    - not atomic among documents
- removing data with `.remove({})` (this is a multidoc operation--passing in an empty query will remove *all documents*)
    - not atomic among documents
- `.drop()` removes all documents, indexes, etc. from a collection
    - vastly faster than `.remove()`, but drops indexes, etc., too (`.remove` does not)

## Error Handling
- the shell automatically checks for errors after every command
- `db.runCommand({ getLastError: 1 })`
    - gives more details about the last command
        - tells you if an upsert was an update or insert
        - tells you how many docs were updated in a multi-update
        - tells you how many docs were removed with a `remove()` operation
        - error details if an error occurred

## Pymongo
- `find({ 'qeury': value })`
- `find_one({ 'qeury': value })`
- queries
- projections (second argument to `find`/`find_one`)
- importing data from reddit
- regular expressions
- `skip`, `limit`, `sort`
- `insert`
- upserts

## Blog project
- project goals (this week)
    - registration
	- login
	- welcome
	- logout
- implementation details
    - cookies
	- requests
	- redirects
- collections
	- posts
	- sessions
	- users
- files
	- controllers
	- views

