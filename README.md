# Project: Cooking time estimation base on food recipe 
## Deployed web application using Azure Web Services: https://cooking-time-prediction.azurewebsites.net/
## Run in local
Create .env file under code folder, put 
```bash
ENDPOINT = http://20.53.169.140:80/api/v1/service/predict-cooking-time/score
KEY = gMGAX6u7vRZKWu24RZQchF696U8mJ6X5
```
In the .env file
Under code directory, run 
```bash
flask run
```
Then the web application can be accessed via localhost:5000
## My idea, approach and implementation
### Idea formation

With a new and unfamiliar recipe, understanding the entire cooking time is essential for the home cook to well prepare before lunch or dinner time. This project aims to build a web application where users can upload a random recipe and the web application will automatically analyse the recipe, aiming to predict the cooking time based on steps, ingredients and other information of the recipe.

AI especially machine learning techniques can be applied to solve this problem. We can predict the cooking time using a machine learning estimator. A machine learning estimator can predict something (such as cooking time for this project) with user input data based on the previously collected data. A machine learning model is trained for prediction using the data from a popular food website (food.com). The data in food.com contains the recipe for many dishes followed by their total cooking time.

