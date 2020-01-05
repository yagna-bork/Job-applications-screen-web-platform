import NeutralNetworkPackage.NetworkClass, NeutralNetworkPackage.database_functions
import random
import sys
sys.path.append("/Users/nathanbailey/OneDrive/Uni/Year2/Term2/CS261/GroupProject/Code/Project/Database")
import database_interface

database = database_interface.Database()


x = NeutralNetworkPackage.NetworkClass.NeutralNetwork()

database.get_applications(1)


# predict = x.create_scores('{"Name": "Denita Abaya", "Degree Qualification": "Economic Studies and Global Sustainable Development, BA", "Degree Level": "2:2", "University Attended": "University of Liverpool", "A-Level Qualifications": [{"Subject": "Engineering ", "Grade": "B"}, {"Subject": "Portuguese ", "Grade": "B"}, {"Subject": "Japanese ", "Grade": "B"}, {"Subject": "Food Technology ", "Grade": "B"}], "Languages Known": [{"Language": "C#", "Expertise": 4}, {"Language": "C++", "Expertise": 0}, {"Language": "Java", "Expertise": 2}], "Previous Employment": [{"Company": "Shoreline", "Position": "Module Lead", "Length of Employment": "1 year 9 months"}, {"Company": "Gekko and Co.", "Position": "software developer", "Length of Employment": "1 year 9 months"}], "Skills": [{"Skill": "Public Speaking", "Expertise": 3}, {"Skill": "Motivated", "Expertise": 6}, {"Skill": "Search engine optimization", "Expertise": 7}, {"Skill": "Text Editing", "Expertise": 1}, {"Skill": "Quality Assurance", "Expertise": 1}, {"Skill": "Skype", "Expertise": 7}, {"Skill": "Video Editing", "Expertise": 2}], "Hobbies": []}',1, 1)





# questions_selected = database.create_test(1, 1)



# json = '[{"QuestionId" : 1, "OptionGiven" : 3},{"QuestionId" : 2, "OptionGiven" : 1}, {"QuestionId" : 3, "OptionGiven" : 4}]'

# returned = database.score_test(json, 1)


# json = '{"Degree" : 20, "A-Levels" : 33,"Languages" : 51, "Employment" : 23, "Skills" : 33, "Response" : 2}'



# questions_selected = database.create_test(1, 1)



# json = '[{"QuestionId" : 1, "OptionGiven" : 3},{"QuestionId" : 2, "OptionGiven" : 1}, {"QuestionId" : 3, "OptionGiven" : 4}]'

# returned = database.score_test(json, 1)
# x.retrain_neutral_network(json,1,1)
