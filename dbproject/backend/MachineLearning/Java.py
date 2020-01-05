import CreateScores
import NeutralNetwork
import createdata
from random import randint

def create_network():

    important_languages = ['java', 'jvm'] 
   
    languages = ['haskell', 'elixir', 'elm', 'f#', 'idris', 'clojure', 'sql', 'nosql', 'hadoop']
    
    important_skills = []
    # print("HI")
    skills = ['behaviour driven development', 'trade lifecycles', 'regulation', 'risk', 'accounting', 'domain driven design', 'graph databases', 'scrum', 'xp', 'kanban', 'agile', 'cqrs']
    
    
    previous_employment = ['software developer', 'scrum master', 'software lead', 'lead developer', 'accounting', 'risk', 'business']
    
    degrees = ['maths', 'engineering', 'computer science', 'chemistry', 'physics', 'business', 'economics']

    data = CreateScores.parse_json('cvDatasetTesting.json')

    scores = CreateScores.create_scores(important_languages, important_skills, languages, skills, degrees, previous_employment, data)

    # print(scores)

    


    NeutralNetwork.create_neutral_network(scores, createdata.java, "Java")


create_network()

# x_data, y_data = create_network()
# test_data = [[40, 11, 5760, 0, 0]]
# res = NeutralNetwork.predict(test_data, 'Java')

# # print(x_data)

# NeutralNetwork.retrain_neutral_network(x_data, y_data, 'Java')

# res1 = NeutralNetwork.predict(test_data, 'Java')

# # print(res)
# # print(res1)