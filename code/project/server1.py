from flask import Flask, jsonify, request, abort
from filmDAO import filmDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

#@app.route('/')
#def index():
  #  return "Hello, World!"

@app.route('/films')
def getAll():
    results = filmDAO.getAll()
    return jsonify(results)

#curl http://127.0.0.1:5000/films/2
@app.route('/films/<int:id>')
def findById(id):
    foundFilm = filmDAO.findById(id)

    return jsonify(foundFilm)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"Due Date\",\"Year\":2001,\"Budget\":60000000,\"Director\":\"Todd Phillips\"}" http://127.0.0.1:5000/films
@app.route('/films', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)
    
    film = {
        "Title": request.json['Title'],
        "Year": request.json['Year'],
        "Budget": request.json['Budget'],
        "Director": request.json['Director'],
    }
    values = (film['Title'], film['Year'], film['Budget'], film['Director'])
    newId = filmDAO.create(values)
    film['id'] = newId
    return jsonify(film)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Budget\":70000000}" http://127.0.0.1:5000/films/1
@app.route('/films/<int:id>', methods=['PUT'])
def update(id):
    foundFilm = filmDAO.findByID(id)
    if not foundFilm:
        abort(404)
    
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

    values = (foundFilm['Title'], foundFilm['Year'], foundFilm['Budget'], foundFilm['Director'], foundFilm['id'])
    filmDAO.update(values)
    return jsonify(foundFilm)

#curl -X DELETE http://127.0.0.1:5000/films/5
@app.route('/films/<int:id>', methods=['DELETE'])
def delete(id):
    filmDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)