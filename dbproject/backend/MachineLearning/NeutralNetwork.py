from json import *
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
import urllib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.exceptions import UndefinedMetricWarning
import pandas as pd
import pickle


def create_neutral_network(x_data, y_data, name):

    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.3)
    scaler = MinMaxScaler()
    scaler.fit(x_data)
    x_test = scaler.transform(x_test)
    x_train = scaler.transform(x_train)
    
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10, 10, 10, 10, 10, 10), activation = 'identity', max_iter=3000)


    mlp.fit(x_train, y_train)
    predictions = mlp.predict(x_test)

    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))
    filename = name+"Network.sav"
    filename2 = name+"Scalar.sav"


    pickle.dump(mlp, open(filename, 'wb'))
    pickle.dump(scaler, open(filename2, 'wb'))

    



    

def retrain_neutral_network(new_data_x, new_data_y, name):
    loaded_neutral_network = pickle.load(open(name+"Network.sav", 'rb'))

    loaded_neutral_network.partial_fit(new_data_x, new_data_y)

    filename = name+"Network.sav"

    pickle.dump(loaded_neutral_network, open(filename, 'wb'))


def predict(x_data, name):
    loaded_neutral_network = pickle.load(open(str(name)+"Network.sav", 'rb'))

    loaded_scaler = pickle.load(open(str(name)+"Scalar.sav", 'rb'))

    x_data = loaded_scaler.transform(x_data)

    return loaded_neutral_network.predict(x_data)
