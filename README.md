# Crop-Recommendation-Using-Machine-Learning
This simple project will provide advice on which crops are best suited to a given area's climate, soil composition, and other factors. This project uses  Machine Learning algorithms to train a model with enough data, and then employs that model to advise the user on the crop that will thrive in the environment they specify.

## Training the Model
### Dataset
The data used in this project is made by augmenting and combining various publicly available datasets of India like weather, soil, etc. You can access the dataset here. This data is relatively simple with very few but useful features unlike the complicated features affecting the yield of the crop.

<b>Attributes information:</b>
<ul>
<li> N - Ratio of Nitrogen content in soil</li>
<li> P - Ratio of Phosphorous content in soil</li>
<li> K - Ratio of Potassium content in soil</li>
<li> Temperature - temperature in degree Celsius</li>
<li> Humidity - relative humidity in %</li>
<li> ph - ph value of the soil</li>
<li> Rainfall - rainfall in mm</li>
</ul>

### ML Algorithms
Five different models are used to train and test the data.

<ul>
<li> Decision Tree - 90% Accuracy</li>
<li> Guassian Naive Bayes - 99.09% Accuracy</li>
<li> Support Vector Machine (SVM) - 10.68% Accuracy</li>
<li> Logistic Regression - 95.22% Accuracy</li>
<li> Random Forest - 99.09% Accuracy</li>
</ul>

Codes for the training part is present in the file <b>Training.ipynb</b>. Download the file ans open it with colab or jupyter Notebook to train and test the model.
We have tarined the 5 models and saved them in pickle file format, which can be used later to predict/recommend the crop type. The saved models are also added to this repository.


## Crop Recommender
The crop-recommendation code, which makes use of the previously saved models, is included in the <b>main.py</b> file. The user inputs data such as Nitogrn amount, rainfall,temperature, and our model determines which crop would thrive under these conditions.

### Technologies
<ul>
<li>Python 3.10.8</li>
<li>Numpy 1.23.4</li>
<li> Scikit-learn 1.1.3 </li>
<li>Tkinter</li>
</ul>

### Setup
Clone this repo and use any python interpreter to run this code. Make sure all the downloaded files are in the same folder.
Also make sure to run the below commands to add the necessary libraries to your project.

<ul>
<b><li> pip install numpy </li>
<li> pip install pickle5 </li>
<li> python -m pip install scikit-learn </li></b>
</ul>

### Demo
This is a simple demo to show you how to use the app. Run the code in a python interpreter, then a GUI will appear as shown in the video.

https://user-images.githubusercontent.com/18510244/201470173-62ce8a4a-a1b7-4afd-8903-2c2711c58ff2.mp4

