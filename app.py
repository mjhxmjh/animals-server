from flask import Flask, request, jsonify, current_app
from flask.json import JSONEncoder

app = Flask(__name__, static_url_path='')

animals = []

@app.route("/")
def hello():
  return  current_app.send_static_file('index.html')

@app.route("/html")
def someHtml():
    return "<html><head></head><body><h1>YEAH</h1></body></html>"

@app.route("/news")
def someNews():
    return "<html><head></head><body><h1>Prince ANdrew's a pedo</h1></body></html>"

@app.route("/form")
def aForm():
    return current_app.send_static_file('form.html')

@app.route("/animal")
def getAnimal():
    animal = Animal()
    animal.name = "Tiger"
    return jsonify(animal)

@app.route("/animalPage")
def getAnimalPage():
    return current_app.send_static_file('animals.html')


@app.route('/animal', methods=['POST'])
def add_message():
    content = request.json
    myNewAnimal = Animal()
    myNewAnimal.name = content['name']
    myNewAnimal.power = content['jsonPower']
    animals.append(myNewAnimal)
    return jsonify(animals)

@app.route('/animals')
def get_my_fucking_animals():
    return jsonify(animals)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Animal):
            return obj.__dict__
        return JSONEncoder.default(self, obj)


class Animal():
    name: str
    power: int

app.json_encoder = CustomJSONEncoder

if __name__ == "__main__":
  app.run(host='localhost', port=9500)