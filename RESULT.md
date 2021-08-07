# Results, Findings and Reflection

## Project Result/Product
A web application is developed, tested and deployed as a result of this project. The website aims for helping predicting the cooking time for a specific recipe. The prediction is implemented using the Azure Machine Learning service. The web application mainly relies on the endpoint (REST service) provided by the Azure Machine Learning service.

To access the depolyed website: https://cooking-time-prediction.azurewebsites.net/

Or a local version can be downloaded following the steps in README.md

Exceptions may occur due to the down of Azure Machine Learning service, please email me to inform if you face this scenario.

## Model result
For labels(the feature we want to predict) in this project, there are three distinct values (1.0, 2.0 and 3.0). So I choose a multi-class classification model (multi-class boosted decision tree). The trained model is evaluated with the unseen testing data set. The overall accuracy is 0.762, which is desirable. My model performs well when predicting labels 1.0 and 2.0, but is unsatisfactory when predicting label 3.0. This may be caused by limited instances with label 3.0 in the dataset.

## Findings and Reflection
Through this project, I experienced in developing a web application that uses Azure Machine Learning service from scratch, understanding how machine learning models are developed and implemented in Azure ML studio and how to utilise Azure services via endpoint (RESTful API call). By doing Microsoft Learning paths and completing this project, I better understand how to use Flask to develop a web application. Besides, I practise documentation along with the lifespan of the project, from formulating the question, proposing a solution, implementation to product delivering. 

The unsatisfactory performance when predicting instances with label 3.0 reminds me of the importance of dataset balancing. Unbalanced data may lead to underperformance when predicting some labels. 
