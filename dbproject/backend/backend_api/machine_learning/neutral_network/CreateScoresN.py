import json



top_universities = ['university of oxford', 'university of cambridge', 'imperial college london', 'ucl', 'university of edinburgh', 'kings college london', 'university of manchester', 'university of bristol', 'university of warwick', 'university of glasgow', 'university of sheffield', 'durham university', 'university of birmingham', 'university of southampton', 'university of york', 'stanford university', 'harvard university', 'caltech', 'mit', 'university of chicago', 'cornell university', 'university of michigan', 'the university of tokyo']


def create_scores(important_languages, important_skills, languages, skills, degrees, previous_employment, data):
    #Create a score for the applicant
    listofscores = []
    k = data
    scores2 = []

    bad_employment = False

    scores = []

    scorelang = 0
    scoreskills = 0
    score_alevels = 0
    scoredegree = 0
    score_employment = 0

    count_important_lang = 0

    count_important_skills = 0



    if len(important_languages) > 0:
        for i in important_languages:
            old_score = scorelang
            for j in k["LanguagesKnown"]:
                lang = j["Language"].strip().lower()
                if lang == i:
                    scorelang += j["Expertise"]*240
            if scorelang == old_score:
                count_important_lang+=1
        
    

        if count_important_lang < len(important_languages):
            for i in k["LanguagesKnown"]:
                lang = i["Language"].strip().lower()
                for j in languages:
                    if lang == j:
                        scorelang += i["Expertise"]*240
    
        
    else:
        for i in k["LanguagesKnown"]:
                lang = i["Language"].strip().lower()
                for j in languages:
                    if lang == j:
                        scorelang += i["Expertise"]*240  



    
    if len(important_skills) > 0:
        for i in important_skills:
            old_score = scoreskills
            for j in k["Skills"]:
                skill = j["Skill"].strip().lower()
                if skill == i:
                    scoreskills += j["Expertise"]*240
            if scoreskills == old_score:
                count_important_skills+=1



        if count_important_skills < len(important_skills):
            for i in k["Skills"]:
                skill = i["Skill"].strip().lower()
                for j in skills:
                    if skill == j:
                        scoreskills += i["Expertise"]*240


    else:
        for i in k["Skills"]:
            skill = i["Skill"].strip().lower()
            for j in skills:
                if skill == j:
                    scoreskills += i["Expertise"]*240


    

    degree = k["DegreeQualification"].strip().lower()
    for j in degrees:
        if j in degree:
            scoredegree += 40

    if k["DegreeLevel"] == '1st':
        scoredegree += 30
    elif k["DegreeLevel"] == '2:1':
        scoredegree += 2

    university = k["UniversityAttended"].strip().lower()

    for i in top_universities:
        if i == university:
            scoredegree+=20

    for i in k["PreviousEmployment"]:
        position = i["Position"].strip().lower()
        for j in previous_employment:
            if j in position:
                score_employment += 30

    # print(score_employment)


    #Negate the score if not in each employment for that long
    if len(k["PreviousEmployment"]) >= 3:
        count = 0
        for i in k["PreviousEmployment"]:
            duration = i["LengthOfEmployment"].strip().lower().replace(" ","")
            if duration.find("year") == -1:
                if duration.find("month") != -1:
                    months_worked = duration[duration.find("month")-1:duration.find("month")]
                    count+=1

            if duration.find("year") == -1:
                if duration[:1] == 1:
                    if duration.find("month") != -1:
                        months_worked = duration[duration.find("month")-1:duration.find("month")]
                        if months_worked < 4:
                            count+=1

            if count == len(k["PreviousEmployment"]):
                bad_employment = True
                score_employment += -20

    for i in k["ALevelQualifications"]:
        if i["Grade"] == "A*":
            score_alevels += 10
        elif i["Grade"] == "A":
            score_alevels += 5
        elif i["Grade"] == "B":
            score_alevels += 1

    scores = [scoredegree, score_alevels, scorelang, score_employment, scoreskills]
    listofscores.append(scores)

    return listofscores, bad_employment

def create_feedback(important_languages, important_skills, languages, skills, degrees, previous_employment, data):
    languages_app = []
    skills_app = []
    employment = []
    correct_employment = []
    for i in data["LanguagesKnown"]:
        languages_app.append(i["Language"].strip().lower())

    for i in data["Skills"]:
        skills_app.append(i["Skill"].strip().lower())

    for i in data["PreviousEmployment"]:
        employment.append(i["Position"].strip().lower())


    important_languages_matched = set(languages_app) & set(important_languages)

    important_languages_not_matched = set(important_languages) - set(languages_app)

    important_skills_matched = set(skills_app)  & set(important_skills)

    important_skills_not_matched = set(important_skills) - set(skills_app)

    languages_matched = set(languages_app) & set(languages)

    languages_not_matched = set(languages) - set(languages_app)

    skills_matched = set(skills_app) & set(skills)


    skills_not_matched = set(skills) - set(skills_app)

    for i in employment:
        for j in previous_employment:
            if j in i:
                correct_employment.append(j)

    employment_matched = correct_employment

    employment_not_matched = set(previous_employment) - set(employment_matched)

    skills_not_matched = list(skills_not_matched)
    skills_matched = list(skills_matched)

    important_languages_matched = list(important_languages_matched)
    important_languages_not_matched = list(languages_not_matched)

    important_skills_matched = list(important_skills_matched)
    important_skills_not_matched = list(important_skills_not_matched)


    languages_matched = list(languages_matched)
    languages_not_matched = list(languages_not_matched)

    employment_matched = list(employment_matched)
    employment_not_matched = list(employment_not_matched)


    skills_match_dict = {}
    for i in range(len(skills_matched)):
        skills_match_dict["Skill"+str(i)] = skills_matched[i]

    skills_not_match_dict = {}
    for i in range(len(skills_not_matched)):
        skills_not_match_dict["Skill"+str(i)] = skills_not_matched[i]

    important_skills_match_dict = {}
    for i in range(len(important_skills_matched)):
        important_skills_match_dict["Skill"+str(i)] = important_skills_matched[i]

    important_skills_not_match_dict = {}
    for i in range(len(important_skills_not_matched)):
        important_skills_not_match_dict["Skill"+str(i)] = important_skills_not_matched[i]


    languages_match_dict = {}
    for i in range(len(languages_matched)):
        languages_match_dict["Language"+str(i)] = languages_matched[i]

    languages_not_match_dict = {}
    for i in range(len(languages_not_matched)):
        languages_not_match_dict["Language"+str(i)] = languages_not_matched[i]

    important_languages_match_dict = {}
    for i in range(len(important_languages_matched)):
        important_languages_match_dict["Language"+str(i)] = important_languages_matched[i]

    important_languages_not_match_dict = {}
    for i in range(len(important_languages_not_matched)):
        important_languages_not_match_dict["Language"+str(i)] = important_languages_not_matched[i]


    employment_match_dict = {}
    for i in range(len(employment_matched)):
        employment_match_dict["Employment"+str(i)] = employment_matched[i]
    
    employment_not_match_dict = {}
    for i in range(len(employment_not_matched)):
        employment_not_match_dict["Employment"+str(i)] = employment_not_matched[i]

    json_data = {"important languages matched": [important_languages_match_dict], "important langauges not matches": [important_languages_not_match_dict], "languages matched": [languages_match_dict], "languages not matched": [languages_not_match_dict], "important skills matched": [important_skills_match_dict], "important skills not matched": [important_skills_not_match_dict], "skills matched": [skills_match_dict], "skills not matched": [skills_not_match_dict], "employment matched": [employment_match_dict], "employment not matched": [employment_not_match_dict]}

    json_data = json.dumps(json_data)


    return json_data
