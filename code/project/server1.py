from flask import Flask, jsonify, request, abort
from filmDAO import filmDAO

app = Flask(__name__, static_url_path='', static_folder='.')

films = [{ "id":1, "Title":"Toy Story", "Year":1995, "Budget":30000000, "Director":"John Lasseter"},
    { "id":2, "Title":"Heat", "Year":1995, "Budget":60000000, "Director":"Michael Mann"},
    { "id":3, "Title":"Casino", "Year":1995, "Budget":52000000, "Director":"Martin Scorsese"}
]
nextId=4


#app = Flask(__name__)

#@app.route('/')
#def index():
  #return "Hello, World!"

#curl "http://127.0.0.1:5000/films"
@app.route('/films')
def getAll():
    results = filmDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/films/2"
@app.route('/films/<int:id>')
def findById(id):
    foundFilm = filmDAO.findById(id)

    return jsonify(foundFilm)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"Elf\",\"Year\":2002,\"Budget\":11000000,\"Director\":\"Jon Favreau\"}" http://127.0.0.1:5000/films
@app.route('/films', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    # other checking 
    film = {
        "id": nextId,
        "Title": request.json['Title'],
        "Year": request.json['Year'],
        "Budget": request.json['Budget'],
        "Director": request.json['Director'],
    }
    nextId += 1
    films.append(film)
    return jsonify(films)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"The Family\",\"Year\":2013,\"Budget\":30000000,\"Director\":\"Jesse Moss\"}" http://127.0.0.1:5000/films/1
@app.route('/films/<int:id>', methods=['PUT'])
def update(id):
    foundFilms = list(filter(lambda t: t['id']== id, films))
    if (len(foundFilms) == 0):
        abort(404)
    foundFilm = foundFilms[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Budget' in reqJson and type(reqJson['Budget']) is not int:
        abort(400)
    if 'Year' in reqJson and type(reqJson['Year']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundFilm['Title'] = reqJson['Title']
    if 'Year' in reqJson:
        foundFilm['Year'] = reqJson['Year']
    if 'Budget' in reqJson:
        foundFilm['Budget'] = reqJson['Budget']
    if 'Director' in reqJson:
        foundFilm['Director'] = reqJson['Director']
 
 
    return jsonify(foundFilm)
        

    return "in update for id "+str(id)


#curl -X DELETE "http://127.0.0.1:5000/films/1"
@app.route('/films/<int:id>' , methods=['DELETE'])
def delete(id):
    foundFilms = list(filter(lambda t: t['id']== id, films))
    if (len(foundFilms) == 0):
        abort(404)
    films.remove(foundFilms[0])
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)