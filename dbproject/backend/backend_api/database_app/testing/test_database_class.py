import mysql.connector
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursorPrepared
from random import randint
import json
import sys
sys.path.append("/Users/nathanbailey/OneDrive/Uni/Year2/Term2/CS261/GroupProject/Code/Project/Database")
import database_interface
import pytest


def test_create_users():
    database = database_interface.Database()
    database.createUser('test', 'test@site.com', 'password123')


def test_login():
    database = database_interface.Database()
    if database.loginVerification('test@site.com', 'password123') != True:
        assert False

def test_job():
    database = database_interface.Database()
    database.createJob('Software Engineer', 'Pass CS261', 'test', 'test', '[{JSON string}]', 'test', '2:1 in Computer Science', True, 'London')

def test_application():
     database = database_interface.Database()
     database.createApplication(1,1,'Computer Science','Warwick','2:1','[{"Subject": "Maths", "Grade": "A*"}]','[{"Language": "Visual Basic .NET", "Expertise": 9}]','[{More JSON}]', '[{More JSON}]', '[{More JSON}]', 'response txt', 'feedback txt', 'cover letter blob', [1.5, 1.6, 2.34, 6.7, 1.09])

def test_create_score_test():
    database = database_interface.Database()
    stuff = database.create_test(1, 1)
    print(stuff)
    database.score_test('[{"QuestionId" : 1, "OptionGiven" : "b"},{"QuestionId" : 2, "OptionGiven" : "a"}, {"QuestionId" : 3, "OptionGiven" : "d"}]', 1)

def test_get_interviews():
    database = database_interface.Database()
    database.get_new_interviews()

def test_feedback_given():
    database = database_interface.Database()
    database.feedback_given(1, '{"Degree" : 20, "A-Levels" : 33,"Languages" : 51, "Employment" : 23, "Skills" : 33, "Response" : 2}')

def test_add_feedback():
    
    database = database_interface.Database()
    database.add_to_feedback(1, 1, 1)

