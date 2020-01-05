import fpdf as pyfpdf
import datetime
import NeutralNetworkPackage.database_functions
import json

import smtplib
import sys

sys.path.append("/Users/nathanbailey/OneDrive/Uni/Year2/Term2/CS261/GroupProject/Code/Project/Database")
import database_interface




Database = database_interface.Database()
now = datetime.datetime.now()

pdf = pyfpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", 'B', size=15)
pdf.cell(200, 7, txt="Report to Deutsche Bank", ln=1, align="C")
pdf.cell(200, 7, txt="Applicants recommeneded for an interview", ln=1, align="C")
date = now.strftime("%d/%m/%Y")
pdf.cell(200, 7, txt=date, ln=1, align="C")



data = Database.get_new_interviews()
pdf.set_font("Arial", 'B', size=12)
for row in data:
    pdf.cell(0, 5, txt="Application: ", ln=1, align="L")
    pdf.set_font("Arial", size=9)
    pdf.cell(0, 5, txt="Degree: "+row[2], ln=1, align="L")
    pdf.cell(0, 5, txt="University: "+row[3], ln=1, align="L")
    pdf.cell(0, 5, txt="Degree Level: "+row[4], ln=1, align="L")
    a_levels = json.loads(row[5])

    for k in a_levels:
        pdf.cell(0, 5, txt="A Level: "+k["Subject"]+", Grade: "+k["Grade"], ln=1, align="L")

    languages = json.loads(row[6])

    for k in languages:
        pdf.cell(0, 5, txt="Language: "+k["Language"]+", Expertise: "+str(k["Expertise"]), ln=1, align="L")

    employment = json.loads(row[7])

    for k in employment:
        pdf.cell(0, 5, txt="Company: "+k["Company"]+", Position: "+k["Position"], ln=1, align="L")

    skills = json.loads(row[8])

    for k in skills:
        pdf.cell(0, 5, txt="Skill: "+k["Skill"]+", Expertise: "+str(k["Expertise"]), ln=1, align="L")

    hobbies = json.loads(row[9])

    for k in hobbies:
        pdf.cell(0, 5, txt="Name: "+k["Name"]+", Interest: "+str(k["Interest"]), ln=1, align="L")

    feedback = json.loads(row[11])
    pdf.cell(0, 10, txt="", ln=1, align="L")
    pdf.cell(0, 5, txt="Why the applicant was chosen for the job", ln=1, align="L")
    pdf.cell(0, 3, txt="", ln=1, align="L")
    pdf.cell(0, 5, txt="Languages matched: ", ln=1, align="L")
    for i in range(len(feedback["important languages matched"])):
        if feedback["important languages matched"][i] != {}:
            lang = feedback["important languages matched"][i]["Language "+str(i)]
            pdf.cell(0, 5, txt=lang.title(), ln=1, align="L")

    for i in range(len(feedback["languages matched"])):
        if feedback["languages matched"][i] != {}:
            lang = feedback["languages matched"][i]["Language "+str(i)]
            pdf.cell(0, 5, txt=lang.title(), ln=1, align="L")
    pdf.cell(0, 3, txt="", ln=1, align="L")
    pdf.cell(0, 5, txt="Skills matched: ", ln=1, align="L")

    for i in range(len(feedback["important skills matched"])):
        if feedback["important skills matched"][i] != {}:
            lang = feedback["important skills matched"][i]["Skill "+str(i)]
            pdf.cell(0, 5, txt=lang.title(), ln=1, align="L")

    for i in range(len(feedback["skills matched"])):
        if feedback["skills matched"][i] != {}:
            lang = feedback["skills matched"][i]["Skill "+str(i)]
            pdf.cell(0, 5, txt=lang.title(), ln=1, align="L")


    pdf.cell(0, 3, txt="", ln=1, align="L")
    pdf.cell(0, 5, txt="Employment matched: ", ln=1, align="L")

    for i in range(len(feedback["employment matched"])):
        if feedback["employment matched"][i] != {}:
            lang = feedback["employment matched"][i]["Employment "+str(i)]
            pdf.cell(0, 5, txt=lang.title(), ln=1, align="L")

    pdf.cell(0, 3, txt="", ln=1, align="L")
    pdf.set_font("Arial", 'B', size=12)
pdf.output("/Users/nathanbailey/OneDrive/Uni/Year2/Term2/CS261/GroupProject/Code/Project/MachineLearning/report.pdf")