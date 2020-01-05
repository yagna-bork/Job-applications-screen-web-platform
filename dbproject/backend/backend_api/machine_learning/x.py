import pytest
import sys
import os
sys.path.append("/Users/nathanbailey/OneDrive/Uni/Year2/Term2/CS261/GroupProject/Code/Project/MachineLearning")

import Java
import Devops
import ui
import qa
import NeutralNetwork
import Hadoop
import full_stack

def test_retrainx():
    x_data, y_data = Java.create_network()
    # print("HI")
    # test_data = [[5, 14, 14, 0, 0]]
    # res = NeutralNetwork.predict(test_data, 'Java')

    # NeutralNetwork.retrain_neutral_network(x_data, y_data, 'Java')

    # res1 = NeutralNetwork.predict(test_data, 'Java')

    # print(res)
    # print(res1)

test_retrainx()

