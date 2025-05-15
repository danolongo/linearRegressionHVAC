# Literature scan on HVAC systems


### What is HVAC?
* "Heating, ventilation, and air conditioning is the use of various technologies to control the temperature, humidity, and purity of the air in an enclosed space. Its goal is to provide thermal comfort and acceptable indoor air quality." (https://en.wikipedia.org/wiki/Heating,_ventilation,_and_air_conditioning)

### Efficiency in HVAC systems
* An efficiency rating in HCAV systems would measure "how well the air conditioner turns electrical energy into cold air." (https://jabertsch.com/hvac-efficiency-ratings-explained/#:~:text=What%20is%20an%20HVAC%20Efficiency,to%20cool%20your%20home%20quickly.)
* Meaning than in our research we will have to understand factors in HVAC that help create more efficient systems through data analysis

# Research

### https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9571769/

* use this quote as a rubric of what not to do when making the model
"First, predominantly, studies focus on the use of individual machine learning models, and ensemble models are not properly investigated. Second, the performance of such models still needs improvement regarding prediction accuracy. Third, often the models are optimized by fine-tuning different hyperparameters, and the potential of feature selection is partially investigated."

* more things to keep in mind; possible ideas to use once assembling the model
"A novel ensemble model is proposed that combines three random forest models (3RF) for predicting the heating and cooling load of the buildings. Performance comparison of the proposed approach is carried out with reference to K-nearest neighbor (KNN), linear regression (LR), random forest (RF), general additive model (GAM), and multilayer perceptron (MLP). In addition, convolutional neural networks (CNN), long short-term memory (LSTM), and their ensemble CNN-LSTM are also used for experiments.

The influence of different features related to building is investigated. The performance of the models is analyzed regarding different features from the dataset such as glazing area, orientation, height, relative compactness, roof area, surface area, and wall area. Mean absolute error, root mean squared error, mean absolute percentage error, and coefficient of determination R-squared is used for performance evaluation."



# The project
This project aims to predict the heating and cooling load of HVAC systems through a variety of parameters and linear regression.
the ipynb file contains a detailed explanation of the logic behind the model, and the py file has the entire model ready to use
