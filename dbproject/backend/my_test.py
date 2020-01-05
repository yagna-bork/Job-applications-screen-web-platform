import sys
sys.path.append('./MachineLearning')
sys.path.append('./Database')

from MachineLearning.NeutralNetworkPackage.NetworkClass import NeutralNetwork
import json

model = NeutralNetwork()
json_object = {
  "Name": "Jaunita Adell", 
  "Degree Qualification": "Physics, MPhys", 
  "Degree Level": "2:1", 
  "University Attended": "Princeton University", 
  "A-Level Qualifications": [
    {"Subject": "Mathematics", "Grade": "A"}, 
    {"Subject": "Japanese ", "Grade": "A"}, 
    {"Subject": "English Language and Literature ", "Grade": "A"}, 
    {"Subject": "Irish ", "Grade": "A"}
  ], 
  "Languages Known": [
    {"Language": "Visual Basic .NET", "Expertise": 9}, 
    {"Language": "Ruby", "Expertise": 9}, 
    {"Language": "C++", "Expertise": 4}, 
    {"Language": "HTML", "Expertise": 6}, 
    {"Language": "Ruby-on-rails", "Expertise": 6}, 
    {"Language": "Executable UML", "Expertise": 8}, 
    {"Language": "UNITY", "Expertise": 4}, 
    {"Language": "TeX", "Expertise": 6}, 
    {"Language": "LaTeX", "Expertise": 6}, 
    {"Language": "High Level Assembly", "Expertise": 9}, 
    {"Language": "Visual Basic", "Expertise": 5}, 
    {"Language": "PostScript", "Expertise": 5}, 
    {"Language": "BASIC", "Expertise": 4}, 
    {"Language": "SQL", "Expertise": 6}, 
    {"Language": "Assembly", "Expertise": 8}, 
    {"Language": "Mathematica", "Expertise": 10}, 
    {"Language": "Perl", "Expertise": 4}, 
    {"Language": "R", "Expertise": 9}
  ], "Previous Employment": [{
      "Company": "Dunder Mifflin", 
      "Position": "Senior Architect", 
      "Length of Employment": "3 years 4 months"
    }], 
    "Skills": [
      {"Skill": "Data Entry", "Expertise": 6}, 
      {"Skill": "Maya", "Expertise": 10}
    ], 
    "Hobbies": [
      {"Name": "Glass blowing", "Interest": 10}
    ]
}
result = model.create_scores(json.dumps(json_object), 1, 1)
print(result[0])
