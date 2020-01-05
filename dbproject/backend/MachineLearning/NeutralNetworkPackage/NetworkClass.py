import sys
sys.path.append("/Users/nathanbailey/OneDrive/Uni/Year2/Term2/CS261/GroupProject/Code/Project/MachineLearning/NeutralNetworkPackage/")
sys.path.append("/Users/nathanbailey/OneDrive/Uni/Year2/Term2/CS261/GroupProject/Code/Project/Database")


from NeutralNetworkPackage import qaN as qa
from NeutralNetworkPackage import DevopsN as Devops
from NeutralNetworkPackage import full_stackN as full_stack
from NeutralNetworkPackage import CreateScoresN as CreateScores
from NeutralNetworkPackage import database_functions as database
from NeutralNetworkPackage import JavaN as Java
from NeutralNetworkPackage import HadoopN as Hadoop
from NeutralNetworkPackage import uiN as ui
import json
import os

import sklearn as sk
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import urllib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
import pandas as pd
import pickle
import database_interface

THIS_FILE = os.path.dirname(__file__) + '/'

class NeutralNetwork:

    def __init__(self):
        self.db = database_interface.Database()

    
    def create_scores(self, data, user_id, job_id):
        job = self.db.get_job_title(job_id)

        dataJSON = json.loads(data)
        important_langauges, important_skills, languages, skills, degrees, previous_employment = self.select_data(job)

        listofscores, bad_employment = CreateScores.create_scores(important_langauges, important_skills, languages, skills, degrees, previous_employment, dataJSON)

        predicted_data, scaled_data = self.predict_data(listofscores, job) 
        scaled_data = scaled_data*100
        data_insert = []

        for i in scaled_data[0]:
            data_insert.append(round(i, 1))
        
        feedback = self.create_feedback(data, job)

        

        id = self.db.createApplication(user_id, job_id, str(dataJSON["Degree Qualification"]), str(dataJSON["University Attended"]), str(dataJSON["Degree Level"]), str(dataJSON["A-Level Qualifications"]), str(dataJSON["Languages Known"]), str(dataJSON["Previous Employment"]), str(dataJSON["Skills"]), str(dataJSON["Hobbies"]), int(predicted_data[0]), str(feedback), 'blob', data_insert)
        
        if predicted_data[0] == 2:
            self.db.add_to_feedback(id, user_id, job_id)

        return predicted_data

    def create_feedback(self, data, job):
        data = json.loads(data)
        important_langauges, important_skills, languages, skills, degrees, previous_employment = self.select_data(job)

        return CreateScores.create_feedback(important_langauges, important_skills, languages, skills, degrees, previous_employment, data)


    def select_data(self, job):
        if job == 'Java':
            return Java.important_languages, Java.important_skills, Java.languages, Java.skills, Java.degrees, Java.previous_employment
        elif job == 'Full Stack':
            return full_stack.important_languages, full_stack.important_skills, full_stack.languages, full_stack.skills, full_stack.degrees, full_stack.previous_employment
        elif job == 'Hadoop':
            return Hadoop.important_languages, Hadoop.important_skills, Hadoop.languages, Hadoop.skills, Hadoop.degrees, Hadoop.previous_employment
        elif job == 'Devops':
            return Devops.important_languages, Devops.important_skills, Devops.languages, Devops.skills, Devops.degrees, Devops.previous_employment
        elif job == 'QA':
            return qa.important_languages, qa.important_skills, qa.languages, qa.skills, qa.degrees, qa.previous_employment
        elif job == 'UI':
            return ui.important_languages, ui.important_skills, ui.languages, ui.skills, ui.degrees, ui.previous_employment
        return None



    def predict_data(self, x_data, job):

        loaded_neutral_network = pickle.load(open(THIS_FILE + str(job)+"Network.sav", 'rb'))

        loaded_scaler = pickle.load(open(THIS_FILE + str(job)+"Scalar.sav", 'rb'))

        x_data = loaded_scaler.transform(x_data)

        return loaded_neutral_network.predict(x_data), x_data

    #2 = interview, 1 = test 0 = rejected

    def json_to_list_scores(self, json_data):
        data = json.loads(json_data)

        return [data["Degree"], data["A-Levels"], data["Languages"], data["Employment"], data["Skills"]], data["Response"]



    def retrain_neutral_network(self, new_data, job_id, application_id):
        job = self.db.get_job_title(job_id)
        loaded_neutral_network = pickle.load(open(job+"Network.sav", 'rb'))

        x_data, y_data = self.json_to_list_scores(new_data)

        loaded_neutral_network.partial_fit([x_data], [y_data])

        filename = job+"Network.sav"

        pickle.dump(loaded_neutral_network, open(filename, 'wb'))

        self.db.feedback_given(application_id, new_data)
