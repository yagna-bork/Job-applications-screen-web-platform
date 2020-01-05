import CreateScores
import NeutralNetwork
import createdata


def create_network():

    important_languages = [] 

    languages = ['bash', 'ruby', 'python', 'java']

    important_skills = []

    skills = ['scrum', 'kanban', 'xp', 'agile', 'junit', 'selenium', 'nexus', 'git', 'docker', 'paas', 'iaas', 'automated builds', 'team city', 'jenkins', 'bamboo', 'unit test', 'risk', 'regulation', 'leading', 'mentoring', 'teaching', 'management', 'unix', 'linux', 'leading', 'windows']

    degrees = ['business', 'computer science', 'engineering', 'maths', 'economics', 'physics', 'risk', 'accounting', 'business', 'biology', 'chemistry', 'sciences']

    previous_employment = ['management', 'team leading', 'mentoring', 'risk', 'teaching', 'accounting', 'software lead', 'software developer', 'scrum master', 'project lead']


    data = CreateScores.parse_json('cvDatasetTesting.json')

    scores = CreateScores.create_scores(important_languages, important_skills, languages, skills, degrees, previous_employment, data)

    NeutralNetwork.create_neutral_network(scores, createdata.devops, "Devops")

create_network()