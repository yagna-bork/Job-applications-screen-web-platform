import json


top_universities = ['university of oxford', 'university of cambridge', 'imperial college london', 'ucl', 'university of edinburgh', 'kings college london', 'university of manchester', 'university of bristol', 'university of warwick', 'university of glasgow', 'university of sheffield', 'durham university', 'university of birmingham', 'university of southampton', 'university of york', 'stanford university', 'harvard university', 'caltech', 'mit', 'university of chicago', 'cornell university', 'university of michigan', 'the university of tokyo']

def parse_json(filename):
    return json.loads(open(filename).read())

def create_scores(important_languages, important_skills, languages, skills, degrees, previous_employment, data):
    #Create a score for the applicant
    listofscores = []
    scores2 = []
    for k in data:

        scores = []

        scorelang = 0
        scoreskills = 0
        score_alevels = 0
        scoredegree = 0
        score_employment = 0

        count_important_lang = 0

        count_important_skills = 0

        # print(len(important_languages))


        if len(important_languages) > 0:
            for i in important_languages:
                old_score = scorelang
                for j in k["Languages Known"]:
                    lang = j["Language"].strip().lower()
                    if lang == i:
                        scorelang += j["Expertise"]*240
                if scorelang == old_score:
                    count_important_lang+=1
        
            # print(scorelang)
            
       

            if count_important_lang < len(important_languages):
                for i in k["Languages Known"]:
                    lang = i["Language"].strip().lower()
                    for j in languages:
                        if lang == j:
                            scorelang += i["Expertise"]*240
        
          
        else:
            for i in k["Languages Known"]:
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


        

        degree = k["Degree Qualification"].strip().lower()
        for j in degrees:
            if j in degree:
                # print(j)
                scoredegree += 40

        if k["Degree Level"] == '1st':
            scoredegree += 30
        elif k["Degree Level"] == '2:1':
            scoredegree += 2

        # print(scoredegree)


        university = k["University Attended"].strip().lower()

        for i in top_universities:
            if i == university:
                scoredegree+=20
        # print(scoredegree)

        for i in k["Previous Employment"]:
            position = i["Position"].strip().lower()
            for j in previous_employment:
                if j in position:
                    score_employment += 30


        #Negate the score if not in each employment for that long
        if len(k["Previous Employment"]) >= 3:
            count = 0
            for i in k["Previous Employment"]:
                duration = i["Length of Employment"].strip().lower().replace(" ","")
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

                if count == len(k["Previous Employment"]):
                    score_employment += -20

        for i in k["A-Level Qualifications"]:
            if i["Grade"] == "A*":
                score_alevels += 10
            elif i["Grade"] == "A":
                score_alevels += 5
            elif i["Grade"] == "B":
                score_alevels += 1

        scores = [scoredegree, score_alevels, scorelang, score_employment, scoreskills]
        listofscores.append(scores)

    
    return listofscores

