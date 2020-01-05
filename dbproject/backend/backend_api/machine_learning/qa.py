import CreateScores
import NeutralNetwork
import createdata

def create_network():

    important_languages = []

    languages = ['sql', 'java', 'python', 'c', 'c#', 'haskell', 'c++', 'php']

    important_skills = []

    skills = ['unix', 'linux', 'behaviour driven development', 'agile testing', 'unit testing', 'integration testing', 'financial services']

    previous_employment = ['software testing', 'software lead', 'software developer', 'manager']

    degrees = ['maths', 'engineering', 'computer science', 'chemistry', 'physics', 'business', 'economics']

    data = CreateScores.parse_json('cvDatasetTesting.json')

    scores = CreateScores.create_scores(important_languages, important_skills, languages, skills, degrees, previous_employment, data)

    NeutralNetwork.create_neutral_network(scores, createdata.qa, "QA")

create_network()