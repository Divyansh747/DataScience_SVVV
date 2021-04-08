# Import all required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, export_graphviz

print(
'''

Name      : Divyansh Rahangdale
Roll no   : 18100BTCSES02782
Class     : Data Science LAB
Aim       : Write a programme in Python to predict if a person will get heart disease or not

'''
)

# Data Set
data = "heart.csv"


# ROW Label Info
names = [ 'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Read CSE File
dataset = pd.read_csv(data, names=names)

# label data into numeric format
array = dataset.values
X = array[:,0:12]
Y = array[:,12]

# train and test values
# test data size 30% and training data size 70% of Dataset
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.3, random_state=7)

# test data to predict loan status
testing_data = ([[63,1,3,145,233,1,0,150,0,2.3,0,0]])
print("Test Data: {}".format(testing_data))

print()

# Logistic Regression ML classification Algorithm
model = LogisticRegression() 
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy of LogisticRegression: {}".format(accuracy_score(y_test, predictions)))
prediction = model.predict(testing_data)
print("Prediction of LogisticRegression: {}".format(prediction))

print()

# Decision Tree ML classification Algorithm
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy of DecisionTreeClassifier: {}".format(accuracy_score(y_test, predictions)))
prediction = model.predict(testing_data)
print("Predicition of DescisionTreeClassifier: {}".format(prediction))

print()

# Random Forest ML classification Algorithm
model = RandomForestClassifier(n_estimators=100)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
print("Accuracy of RandomForestClassifier: {}".format(accuracy_score(y_test, predictions)))
prediction = model.predict(testing_data)
print("Predicition of RandomForestClassifier: {}".format(prediction))

print(x_test)
