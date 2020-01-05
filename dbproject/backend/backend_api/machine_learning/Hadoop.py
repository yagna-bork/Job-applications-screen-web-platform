import CreateScores
import NeutralNetwork
import createdata


def create_network():

    important_languages = []

    languages = ['java', 'scala', 'python', 'sql', 'oracle', 'bootstrap', 'react', 'css', 'html', 'javascript', 'd3', 'node.js', 'react', 'angular']

    important_skills = ['hadoop']

    skills = ['agile', 'scrum', 'kanban', 'xp', 'test driven development', 'refactoring', 'leading teams', 'mentoring', 'teaching', 'data science', 'pandas', 'relational databases', 'databases', 'risk', 'regulation', 'accounting', 'apache spark']

    previous_employment = ['test driven development', 'data science', 'front end', 'software developer', 'software lead', 'project manager', 'accounting']


    degrees = ['maths', 'engineering', 'computer science', 'chemistry', 'physics', 'business', 'economics']


    data = CreateScores.parse_json('cvDatasetTesting.json')

    scores = CreateScores.create_scores(important_languages, important_skills, languages, skills, degrees, previous_employment, data)

    NeutralNetwork.create_neutral_network(scores, createdata.hadoop, "Hadoop")

create_network()



