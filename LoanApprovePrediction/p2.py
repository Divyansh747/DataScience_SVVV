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
Aim       : Write a programme in Python to predict if a loan will get approved or not
DataSet   : https://raw.githubusercontent.com/callxpert/datasets/master/Loan-applicant-details.csv

'''
)

# Data Set URL (GITHUB LINK)
url = "https://raw.githubusercontent.com/callxpert/datasets/master/Loan-applicant-details.csv"

# ROW Label Info
names = ['Loan_ID','Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area','Loan_Status']

# Read CSE File
dataset = pd.read_csv(url, names=names)

from sklearn.preprocessing import LabelEncoder
var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
le = LabelEncoder()

# label data into numeric format
for i in var_mod:
    dataset[i] = le.fit_transform(dataset[i])
array = dataset.values
X = array[:,6:11]
Y = array[:,12]
Y=Y.astype('int')

# train and test values
# test data size 30% and training data size 70% of Dataset
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.3, random_state=7)

# test data to predict loan status
testing_data = ([[4750,2333,130,360,1]])
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
