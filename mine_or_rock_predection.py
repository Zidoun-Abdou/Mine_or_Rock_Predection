# -*- coding: utf-8 -*-
"""Mine or Rock Predection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FJJSjes6F4Ii0QWdVGHGi1JgUTFjaenk

Import Libraries
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Preprocessing"""

#loading the dataset to pandas dataframe
sonar_data = pd.read_csv('/content/sonar data.csv', header=None)

sonar_data.head()

sonar_data.shape

#show stat measures of data
sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#separating data and target
X = sonar_data.drop(columns=60,axis=1)
Y = sonar_data[60]

print(X)
print(Y)

"""Train and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

model = LogisticRegression()

model.fit(X_train, Y_train)

"""Model Evaluation"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)
print("Accuracy on training data :" ,training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)
print("Accuracy on test data :" ,test_data_accuracy)

"""Making a prediction system"""

input_data = (0.0151,0.0320,0.0599,0.1050,0.1163,0.1734,0.1679,0.1119,0.0889,0.1205,0.0847,0.1518,0.2305,0.2793,0.3404,0.4527,0.6950,0.8807,0.9154,0.7542,0.6736,0.7146,0.8335,0.7701,0.6993,0.6543,0.5040,0.4926,0.4992,0.4161,0.1631,0.0404,0.0637,0.2962,0.3609,0.1866,0.0476,0.1497,0.2405,0.1980,0.3175,0.2379,0.1716,0.1559,0.1556,0.0422,0.0493,0.0476,0.0219,0.0059,0.0086,0.0061,0.0015,0.0084,0.0128,0.0054,0.0011,0.0019,0.0023,0.0062)

#convert input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the data
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)
print(prediction)

