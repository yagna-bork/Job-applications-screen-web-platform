from json import *
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import urllib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
import pandas as pd
import pickle

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

irisdata = pd.read_csv('iris.data', names=names)


x = irisdata.iloc[:, 0:4]
# print(x)
y = irisdata.select_dtypes(include=[object])

le = preprocessing.LabelEncoder()

y = y.apply(le.fit_transform)
#
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

print(x_train)


scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
#
mlp = MLPClassifier(hidden_layer_sizes=(30,20,40), max_iter=1000)
mlp.fit(x_train, y_train.values.ravel())

predictions = mlp.predict(x_test)




print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
#
x_train2 = irisdata.iloc[:, 0:4]
# print(x)
y_train2 = irisdata.select_dtypes(include=[object])

le2 = preprocessing.LabelEncoder()

y_train2 = y.apply(le2.fit_transform)

scaler = StandardScaler()
scaler.fit(x_train2)
x_train2 = scaler.transform(x_train2)

mlp.partial_fit(x_train2, y_train2.values.ravel())

predictions = mlp.predict(x_test)

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
