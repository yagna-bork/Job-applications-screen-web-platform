import json
import csv

data = json.loads(open('cvDatasetNEW.json').read())

num = input("How many CVs do you want to score? ")

scores = []

for i in range(int(num)):

    print("Name: "+ str(data[i]["Name"]))
    print("Degree: "+str(data[i]["Degree Qualification"]))
    print("Degree Level: "+data[i]["Degree Level"])
    print("University: "+data[i]["University Attended"])
    for j in data[i]["A-Level Qualifications"]:
        print("Subject: "+str(j["Subject"]))
        print("Grade: "+str(j["Grade"]))

    for j in data[i]["Languages Known"]:
        print("Language: "+str(j["Language"]))
        print("Expertise: "+str(j["Expertise"]))
    
    for j in data[i]["Previous Employment"]:
        print("Company: "+str(j["Company"]))
        print("Position: "+str(j["Position"]))

    for j in data[i]["Skills"]:
        print("Skill: "+str(j["Skill"]))
        print("Expertise: "+str(j["Expertise"]))

    for j in data[i]["Hobbies"]:
        print("Hobby: "+str(j["Name"]))
        print("Interest: "+str(j["Interest"]))

    print("2 = interview, 1 = tests, 0 = rejected")

    devops = input("Result for Devops: ")
    full_stack = input("Result for full stack: ")
    hadoop = input("Result for hadoop: ")
    java = input("Result for java: ")
    qa = input("Result for qa: ")
    ui = input("Result for ui: ")

    scores.append([str(data[i]["Name"]), devops, full_stack, hadoop, java, qa, ui])


with open('scoresRetrain.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(scores)

csvFile.close()

print("Data written to CSV file!")

newfile = open("cvDatasetNEW.json", "w")
newfile.write("[")
for i in range(int(num), len(data)):
    newfile.write(json.dumps(data[i]))
    if i != len(data)-1:
        newfile.write(",")
    

newfile.write("]")

print("JSON file updated!")



    

