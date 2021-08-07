# Results, Findings and Reflection

## Project Result/Product
A web application is developed, tested and deployed as a result of this project. The website aims for helping predicting the cooking time for a specific recipe. The prediction is implemented using the Azure Machine Learning service. The web application mainly relies on the endpoint (REST service) provided by the Azure Machine Learning service.

To access the depolyed website: https://cooking-time-prediction.azurewebsites.net/

Or a local version can be downloaded following the steps in README.md

Exceptions may occur due to the down of Azure Machine Learning service, please email me to inform if you face this scenario.

## Model result
For labels(the feature we want to predict) in this project, there are three distinct values (1.0, 2.0 and 3.0). So I choose a multi-class classification model (multi-class boosted decision tree). The trained model is evaluated with the unseen testing data set. The overall accuracy is 0.762, which is desirable. My model performs well when predicting labels 1.0 and 2.0, but is unsatisfactory when predicting label 3.0. This may be caused by limited instances with label 3.0 in the dataset.
## Findings and Reflection
Through this project, I conceive 

A lesson I learnt from the unexpected performance of predicting instances with label 3.0 is that 
