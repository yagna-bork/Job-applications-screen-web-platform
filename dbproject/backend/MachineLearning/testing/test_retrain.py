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

def test_retrain():

    #Java data

    x_datajava = [[0.5,        1.,         0.26923077, 0. ,        0.        ],
    [0.5,       0.375,      0.,         0.,         0.        ],
    [0.,         0.5625,     0.,         0.,         0.        ],
    [0.83333333, 0.75,       0.,         0.,         0.        ]]

    y_datajava = [2, 0, 0, 0]

    NeutralNetwork.retrain_neutral_network(x_datajava, y_datajava, 'Java')

    x_datadev = [[1.,         0.5,        0.51515152, 0.5,        0.        ],
    [0.25,       0.625,      0.,         1.,         0.        ],
    [0.375,      0.3125,     0.15151515, 0.,         0.        ],
    [0.25,       0.1875,     0.,         0.,         0.        ]]

    y_datadev = [0, 0, 1, 0]

    NeutralNetwork.retrain_neutral_network(x_datadev, y_datadev, 'Devops')
