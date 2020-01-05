import CreateScores
import NeutralNetwork
import createdata


def create_network():

    important_skills = []

    important_languages = []

    languages = ['css', 'javascript', 'angular', 'bootstrap', 'html', 'react', 'd3', 'node', 'sql', 'nosql', 'java', 'scala']

    skills = ['agile', 'scrum', 'refactoring', 'relational databases', 'test driven development', 'graph databases', 'risk', 'trade lifecycles', 'accounting', 'instruments', 'domain driven design', 'cqrs', 'kanban', 'xp', 'regulation']

    previous_employment = ['accounting', 'management', 'scrum master', 'mentoring', 'teaching', 'leading', 'risk', 'business', 'software developer', 'full stack', 'front end']

    degrees = ['business', 'computer science', 'engineering', 'maths', 'chemistry']

    data = CreateScores.parse_json('cvDatasetTesting.json')

    scores = CreateScores.create_scores(important_languages, important_skills, languages, skills, degrees, previous_employment, data)

    NeutralNetwork.create_neutral_network(scores, createdata.full_stack, "Full_Stack")

create_network()



