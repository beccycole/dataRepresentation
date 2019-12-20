from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

films=[
    { "id":1, "Title":"Toy Story", "Year":1995, "Budget":50000000, "Director":"John Lasseter"},
    { "id":2, "Title":"Casino", "Year":1995, "Budget":60000000, "Director":"Martin Scorsese"},
    { "id":3, "Title":"The Hangover", "Year":2010, "Budget":50000000, "Director":"Todd Phillips"}
]
nextId=4

#app = Flask(__name__)

#@app.route('/')
#def index():
  #  return "Hello, World!"

@app.route('/films')
def getAll():
    return jsonify(films)

#curl http://127.0.0.1:5000/films/2
@app.route('/films/<int:id>')
def findById(id):
    foundFilms = list(filter(lambda t: t['id']==id, films))
    if len(foundFilms) == 0:
        return jsonify ({}) , 204
    return jsonify(foundFilms[0])

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"Due Date\",\"Year\":2001,\"Budget\":60000000,\"Director\":\"Todd Phillips\"}" http://127.0.0.1:5000/films
@app.route('/films', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    
    film = {
        "id": nextId,
        "Title": request.json['Title'],
        "Year": request.json['Year'],
        "Budget": request.json['Budget'],
        "Director": request.json['Director'],
    }
    nextId += 1
    films.append(film)
    return jsonify(film)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Budget\":70000000}" http://127.0.0.1:5000/films/1
@app.route('/films/<int:id>', methods=['PUT'])
def update(id):
    foundFilms = list(filter(lambda t: t['id']== id, films))
    if (len(foundFilms) == 0):
        abort(404)
    foundFilm = foundFilms[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Year' in reqJson and type(reqJson['Year']) is not int:
        abort(400)
    if 'Budget' in reqJson and type(reqJson['Budget']) is not int:
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

#curl -X DELETE http://127.0.0.1:5000/films/5
@app.route('/films/<int:id>', methods=['DELETE'])
def delete(id):
    foundFilms = list(filter(lambda t: t['id']== id, films))
    if (len(foundFilms) == 0):
        abort(404)
    films.remove(foundFilms[0])
    return jsonify({"done":True})



if __name__ == '__main__' :
    app.run(debug= True)