import Java
import CreateScores
import NeutralNetwork
import createdata
from random import randint


for i in range(300):
    x_data, y_data = Java.create_network()
    test_data = [[40, 11, 5760, 0, 0]]
    res = NeutralNetwork.predict(test_data, 'Java')

    # print(x_data)

    NeutralNetwork.retrain_neutral_network(x_data, y_data, 'Java')

    res1 = NeutralNetwork.predict(test_data, 'Java')

    # print(res)
    # print(res1)
    if res != res1:
        print("Retrained")