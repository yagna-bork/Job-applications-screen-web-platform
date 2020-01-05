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

        
def test_create_java():
    Java.create_network()

def test_create_ui():
    ui.create_network()

def test_create_qa():
    qa.create_network()

def test_create_devops():
    Devops.create_network()

def test_create_full_stack():
    full_stack.create_network()

def test_create_hadoop():
    Hadoop.create_network()



