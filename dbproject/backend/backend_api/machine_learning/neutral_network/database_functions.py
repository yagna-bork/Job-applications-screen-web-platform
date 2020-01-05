import mysql.connector
from random import randint
import json


class DatabaseFunctions:

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="caramel",
            database="TEST"
        )

    def count_questions(self, job_id):
        cursor = self.db.cursor()

        sql = "select count(question) from questions where job_id = '"+str(job_id)+"';"

        cursor.execute(sql)
        num_questions = cursor.fetchone()[0]

        cursor.execute("select question, question_id from questions where job_id = '"+str(job_id)+"';")
        questions = []
        for i in cursor.fetchall():
            questions.append([i[0], i[1]])
        return self.select_questions(num_questions, questions)

    def get_job_title(self, job_id):
        cursor = self.db.cursor()
        cursor.execute("select title from jobs where id = '"+str(job_id)+"';")
        job_title = cursor.fetchone()[0]
        return job_title

    def select_questions(self, num, questions):
        numtopick = int(num/2)
        questions_selected = []
        for i in range(numtopick):
            questions_selected.append(questions[randint(0,num-1)])
        return questions_selected

    def create_test(self, job_id, user_id):
        cursor = self.db.cursor()
        questions = self.count_questions(job_id)
        sql = "insert into tests values("+str(user_id)+", NULL, False, NULL)"
        cursor.execute(sql)
        self.db.commit()
        cursor.execute("select test_id from tests order by test_id desc limit 1")
        id = int(cursor.fetchone()[0])
        # print(id)
        for i in questions:
            sql = "insert into testquestions values("+str(id)+", "+str(i[1])+")"
            cursor.execute(sql)
        self.db.commit()
        questions_json = {}
        for i in questions:
            questions_json["QuestionID"] = i[1]
        return json.dumps(questions_json)

    def score_test(self, answers, test_id):
        cursor = self.db.cursor()
        ans = json.loads(answers)
        cursor.execute("select count(question_id) from testquestions where test_id = "+str(test_id))
        num_questions = cursor.fetchone()[0]
        score_q = 100/num_questions
        score = 0
        for i in ans:
            cursor.execute("select correct_answer from questions where question_id = "+str(i["QuestionId"]))
            ans_given = cursor.fetchone()[0]
            if str(ans_given) == str(i["OptionGiven"]):
                score+=score_q
        return json.dumps([{'test_id':int(test_id), 'score':float(score)}])


    def score_test(self, answers, test_id):
        cursor = self.db.cursor()
        ans = json.loads(answers)
        cursor.execute("select count(question_id) from testquestions where test_id = "+str(test_id))
        num_questions = cursor.fetchone()[0]
        score_q = 100/num_questions
        score = 0
        for i in ans:
            cursor.execute("select correct_answer from questions where question_id = "+str(i["QuestionId"]))
            ans_given = cursor.fetchone()[0]
            if str(ans_given) == str(i["OptionGiven"]):
                score+=score_q
        return json.dumps([{'test_id':int(test_id), 'score':float(score)}])


    def get_new_interviews(self):
        cursor = self.db.cursor()

        sql = "select * from UserJobs where userjob_id IN (select application_id from feedback where given_feedback = False)"

        cursor.execute(sql)

        return cursor.fetchall()



        
    
