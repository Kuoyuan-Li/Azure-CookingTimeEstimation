# Project: Cooking time estimation based on food recipe 
## Deployed web application using Azure Web Services: 

https://cooking-time-prediction.azurewebsites.net/
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

## Data terms of use
The data has been collected from Food.com (formerly GeniusKitchen), under the provision that any resulting work should cite this resource:
Generating Personalized Recipes from Historical User Preferences. Bodhisattwa Prasad Majumder, Shuyang Li, Jianmo Ni, Julian McAuley, in Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), 2019.
## My idea, approach and implementation
### Idea formation

With a new and unfamiliar recipe, understanding the entire cooking time is essential for the home cook to well prepare before lunch or dinner time. This project aims to build a web application where users can upload a random recipe and the web application will automatically analyse the recipe, aiming to predict the cooking time based on steps, ingredients and other information of the recipe.

AI especially machine learning techniques can be applied to solve this problem. We can predict the cooking time using a machine learning estimator. A machine learning estimator can predict something (such as cooking time for this project) with user input data based on the previously collected data. A machine learning model is trained for prediction using the data from a popular food website (food.com). The data in food.com contains the recipe for many dishes followed by their total cooking time.

### Approach
A website server and a machine learning model are required for this project. For the machine learning model, the Azure Machine Learning service is used because it provides many useful functionalities and hides the complicated implementation parts. Programmers can simply manipulate the pipeline to develop a model. The first phase of the machine learning lifecycle is data collection, preprocessing and analytics. By deriving the data from food.com, a CSV file contains approximately 40,000 various recipes are created. There are 5 attributes in the file, which are name, number of ingredients, ingredients, number of steps and detailed steps description. The target label (what we want to predict) is the cooking duration. To simplify the model, cooking duration is separated into 3 levels:1.0(fast), 2.0(medium) and 3.0(slow). Because name, steps and ingredients are text data, text encoding preprocessing is significant for later training and predicting. The detailed implementation will be described later. Through analysing the processed data, I found many columns are all of the 0s due to the encoding method, which indicates feature selection should be applied to reduce the dimensions. I decide to use filter-based feature selection because it is provided in pipeline assets. The processed recipe data is ready for model training at this stage.

The second phase of the machine learning lifecycle is modelling. For labels, there are three distinct values (1.0, 2.0 and 3.0), thus a multi-class classification model should be used as a learner. I use the multi-class boosted decision tree to train the model because it is fast and accurate. The trained model is evaluated with the unseen testing data set. The overall accuracy is 0.762, which is a satisfying result. According to the confusion matrix, my model has a great performance on predicting labels 1.0 and 2.0, but is undesirable when predicting label 3.0. This may be caused by limited instances with label 3.0 in the training dataset. After training the model, I create the real-time inference pipeline which is used for prediction. The inference pipeline is deployed on Azure. With the given endpoint and key after deployment, I can utilise the service to predict the cooking time with recipes from users.
![image](https://user-images.githubusercontent.com/66192678/128597651-94f11e99-c2b5-44b3-a986-2d33d0a09b4d.png)

The final phase of the machine learning lifecycle is production. The machine learning service is successfully deployed on Azure and the flask web application can access and utilise it via endpoint and key. Due to subscription limitations, I only use a 4-core CPU which leads to some latency issues. I’ve asked a couple of my friends to try the website and gathered some feedback. Users may need to wait 10-20 seconds before receiving the answer, and longer when the input text is long. This reduces the user experience and usability. Long response time can be improved by adding extra CPUs and memory. 

The website server is implemented using the Flask framework. Users are required to type recipe data, then the web app will revoke the Azure ML endpoint and send user data for prediction. The prediction outcome is displayed on the new webpage.

The scalability and extensibility of this web application are large. The current accuracy is not high, which can be improved by adding more data with label 3.0. The cooking time is represented using discrete labels instead of continuous time. We can collect more recipe data with exact time, then using a regression model to estimate the time in (such as) minutes. Recipes contain all cuisine around the world but the food may vary from place to place. The recipes can be clustered by cuisine types. Multiple models can be trained such that each model corresponds to each cuisine type. This service can be embedded in popular cooking-related websites or forums so global users can use it to estimate the cooking time given a new recipe.

### Implementation
The pipeline designer feature from the Azure machine learning service assembles data preprocessing, analysis, model training, evaluation and deployment in one place. For my model, the first task is to encode text features. “Preprocess Text” is used to remove stop words and redundant characters, normalise cases and lemmatise words in text attributes. “Feature Hashing” is an encoding method to transform the text into vectors. After encoding, more than 3000 columns add. “Filter Based Feature Selection” is applied to select important features and reduce dimensions. The processed dataset is used to train the MultiClass Boosted Decision Tree model. The whole pipeline is 
![image](https://user-images.githubusercontent.com/66192678/128597606-157c2fa6-740a-4f99-9b94-b2c6294ec6cd.png)

"Split data" is used to split the whole dataset into the training part and testing part where the testing part is for evaluation. 

After creating the training pipeline, an inference pipeline (the pipeline for prediction) can automatically create. The inference pipeline deploys on Azure for other services (such as my Flask app) to use.

The flask implementation is simple. Two routers are used for asking input and displaying results respectively. The corresponding HTML files are created under the templates folder. 
