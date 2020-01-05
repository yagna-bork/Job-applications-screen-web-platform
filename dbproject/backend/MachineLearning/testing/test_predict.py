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

jobs = ['Devops', 'Full Stack', 'Hadoop', 'qa', 'UI', 'Java']

def test_predict():
    for j in range(len(jobs)):
        test_data = [[5, 14, 14, 0, 0]]
        res = NeutralNetwork.predict(test_data, jobs[j])
        assert (res == [2]) | (res == [1]) | (res == [0])

        for i in range(4):
            res_new = NeutralNetwork.predict(test_data, jobs[j])
            if res_new != res:
                assert False