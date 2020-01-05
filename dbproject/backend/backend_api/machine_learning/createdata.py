import xlrd
import csv 

workbook = xlrd.open_workbook('cvs_score.xlsx')

worksheet = workbook.sheet_by_index(0)

reponses = []

devops = []
full_stack = []
hadoop = []
java = []
qa = []
ui = []
import pandas as pd

df = pd.read_csv('scores.csv', names=['Names', 'Devops', 'FullStack', 'Hadoop', 'Java', 'QA', 'UI'])


count = 0
for i in range(1,7):
    temp = []
    for j in range(1,worksheet.nrows):
        if str(worksheet.cell(j,i).value).lower() == "go to interview":
            temp.append(2)
        elif str(worksheet.cell(j,i).value).lower() == "further tests":
            temp.append(1)
        elif str(worksheet.cell(j,i).value).lower() == "not accepted":
            temp.append(0)
    reponses.append(temp)


devops = reponses[0]
devops += list(df.Devops)
full_stack = reponses[1]
full_stack += list(df.FullStack)
hadoop = reponses[2]
hadoop += list(df.Hadoop)
java = reponses[3]
java += list(df.Java)
qa = reponses[4]
qa += list(df.QA)
ui = reponses[5]
ui += list(df.UI)


    




