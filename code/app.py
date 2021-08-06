import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    recipeName = request.form['recipeName']
    ingredientsCount = request.form['ingredientsCount']
    ingredients = request.form['ingredients']
    stepsCount = request.form['stepsCount']
    steps = request.form['steps']
    cookingTime = 0
    # Load the values from .env
    #key = os.environ['KEY']
    #endpoint = os.environ['ENDPOINT']
    #location = os.environ['LOCATION']

    # Indicate that we want to translate and the API version (3.0) and the target language

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'result.html',
        recipeName = recipeName,
        cookingTime = cookingTime
    )