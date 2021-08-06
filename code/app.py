import requests, os, json, urllib.request
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    # Index page shows the form for user to fill the recipe details
    return render_template('index.html')



@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    recipeName = request.form['recipeName']
    ingredientsCount = request.form['ingredientsCount']
    ingredients = request.form['ingredients']
    stepsCount = request.form['stepsCount']
    steps = request.form['steps']
    #print (recipeName,ingredientsCount,ingredients,stepsCount,steps)
    cookingTime = 1.0

    # Load the values from .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    #print (key, endpoint)
    # Call ML endpoint, ask the ML model for prediction
    data = {
        "Inputs": {
            "WebServiceInput0":
            [
                {
                    'name': recipeName,
                    'n_ingredients': ingredientsCount,
                    'ingredients': ingredients,
                    'n_steps': stepsCount,
                    'steps': steps
                },
            ],
        },
        "GlobalParameters":  {
        }
    }

    body = str.encode(json.dumps(data))


    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}

    req = urllib.request.Request(endpoint, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        json_result = json.loads(result.decode('utf-8'))
        output = json_result["Results"]["WebServiceOutput0"][0]
        print(output)
        # get answer (cooking time prediction) from the server
        cookingTime = output["cookingTimePrediction"]

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers to help debug
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
    
    # decide speed based on label
    if cookingTime == "1.0":
        cookingTime = "rapidly"
    elif cookingTime == "2.0":
        cookingTime = "neither fast nor slow"
    elif cookingTime == "3.0":
        cookingTime = "slowly"

    # Call render template, passing the recipe name and cooking time to the template
    return render_template(
        'result.html',
        recipeName = recipeName,
        cookingTime = cookingTime
    )