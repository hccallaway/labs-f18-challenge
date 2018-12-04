from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/pokemon/<query>', methods=['GET'])
def listPokemon(query):
    r = requests.get(
        'https://pokeapi.co/api/v2/pokemon/' + query)
    print(r.json())
    # pokeName = r.anme
    # pokeId = r.id
    # return 'The pokemon with id {} is {}'.format(pokeName, pokeId)
    return 'The pokemon with id {} is {}'


if __name__ == '__main__':
    app.run()
