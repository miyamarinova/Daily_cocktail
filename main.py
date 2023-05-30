from flask import Flask, render_template, url_for, request, send_from_directory
import requests
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'akjnddkds'

COCKTAIL_ENDPOINT = "https://www.thecocktaildb.com/api/json/v1/1/random.php"




@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('index.html')


@app.route('/today-cocktail', methods=['POST', 'GET'])
def today_cocktail():
    response = requests.get(COCKTAIL_ENDPOINT)
    response.raise_for_status()
    ingredients = []
    measures = []
    cocktail = response.json()
    print(cocktail['drinks'][0]['strIngredient1'])
    print(cocktail['drinks'][0]['strIngredient2'])
    print(cocktail['drinks'][0]['strIngredient3'])
    print(cocktail['drinks'][0]['strIngredient4'])
    print(cocktail['drinks'][0]['strIngredient5'])
    print(cocktail['drinks'][0]['strIngredient6'])
    print(cocktail['drinks'][0]['strIngredient7'])

    return render_template('today-cocktail.html', cocktail=cocktail,ingredients=ingredients,measures=measures)

def run_app():
    app.run(debug=False, threaded=True)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    first_thread = threading.Thread(target=run_app)
    second_thread = threading.Thread(target=while_function)
    first_thread.start()
    second_thread.start()