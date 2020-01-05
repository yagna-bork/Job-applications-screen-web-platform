import CreateScores
import NeutralNetwork
import createdata

def create_network():

    important_languages = []
    important_skills = []

    languages = ['css', 'html', 'javascript', 'react', 'd3', 'angular', 'sql', 'restapi', 'java']

    skills = ['restapi', 'agile', 'scrum', 'kanban', 'xp', 'behaviour driven development', 'gwt', 'jsf', 'springmvc', 'relational databases', 'risk', 'trade lifecycles', 'accounting']


    previous_employment = ['software testing', 'software lead', 'software developer', 'scrum master', 'front end', 'full stack', 'manager']


    degrees = ['maths', 'engineering', 'computer science', 'chemistry', 'physics', 'business', 'economics']

    data = CreateScores.parse_json('cvDatasetTesting.json')

    scores = CreateScores.create_scores(important_languages, important_skills, languages, skills, degrees, previous_employment, data)


    NeutralNetwork.create_neutral_network(scores, createdata.ui, "UI")

create_network()