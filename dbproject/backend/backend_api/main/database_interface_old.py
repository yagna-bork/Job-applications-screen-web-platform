import mysql.connector
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursorPrepared
from random import randint
import json
import pytest
import datetime

class Database:
    def __init__(self, host='localhost', database='dbproject_db', user='root', password='rootpassword'):
        try:
            self.__connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                use_pure=True  # This stops NotImplementedError when executing prepared statement
            )
        except mysql.connector.Error as error:
            self.__connection.rollback()
            print("Failed to connect {}".format(error))

    def closeConnection(self):
        if(self.__connection.is_connected()):
            self.__cursor.close()
            self.__connection.close()
            # print("MySQL connection is closed")
        else:
            print("No database connections")

    def executeSelect(self, select_statement, select_tuple):
        self.__cursor = self.__connection.cursor(
            cursor_class=MySQLCursorPrepared)
        try:
            self.__cursor.execute(select_statement, select_tuple)
            records = self.__cursor.fetchall()
            if self.__cursor.rowcount == 1:
                return True
            elif self.__cursor.rowcount == 0:
                return False
            else:

                print("Error", self.__cursor.rowcount, "users selected")
                assert False
        except mysql.connector.Error as e:
            raise e
            # assert False
        

    def executeInsert(self, insert_statement, insert_tuple):
        self.__cursor = self.__connection.cursor(
            cursor_class=MySQLCursorPrepared)
        try:
            result = self.__cursor.execute(insert_statement, insert_tuple)
            self.__connection.commit()
            if self.__cursor.lastrowid:
                return self.__cursor.lastrowid
        except mysql.connector.Error as error:

            self.__connection.rollback()
            raise error
            # assert False
            

    def createUser(self, firstname, lastname, email, hashed_password):
        insert_statement = "INSERT INTO users (firstname, lastname, email, hashed_password) VALUES (%s, %s, %s, %s)"
        insert_tuple = (firstname, lastname, email, hashed_password)
        return self.executeInsert(insert_statement, insert_tuple)

    def createJob(self, title, description, responsibilities, people_management, skills_needed, ideal_candidate, education, available, location):
        insert_statement = "INSERT INTO jobs(title, description, responsibilities, people_management, skills_needed, ideal_candidate, education, available, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        insert_tuple = (title, description, responsibilities, people_management,
                        skills_needed, ideal_candidate, education, available, location)
        return self.executeInsert(insert_statement, insert_tuple)

    def createApplication(self, user_id, job_id, degree, university, degree_level, a_levels, languages, employment, skills, hobbies, response, feedback, cover_letter, scores):
        # Take in strings, JSON strings and list of floats
        insert_statement = "INSERT INTO userjobs (user_id, job_id, degree, university, degree_level, a_levels, languages, employment, skills, hobbies, response, feedback, cover_letter, score_degree, score_alevels, score_lang, score_employment, score_skills, userjob_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        insert_tuple = (user_id, job_id, degree, university, degree_level, a_levels, languages, employment, skills,
                        hobbies, response, feedback, cover_letter, scores[0], scores[1], scores[2], scores[3], scores[4], None)
        return self.executeInsert(insert_statement, insert_tuple)

    def add_to_feedback(self, application_id, user_id, job_id):
        cursor = self.__connection.cursor()
        sql = "insert into feedback values("+str(user_id) + \
            ","+str(job_id)+"," + str(application_id)+", False)"
        cursor.execute(sql)
        self.__connection.commit()

    def loginVerification(self, email, password):
        cursor = self.__connection.cursor()
        # In the actual version you would simply pass the hashed version and compare it to the same value
        # Since the password is stored in plaintext, the code will remain the same
        # (though the variable name could be changed to hashed_password for clarity)
        select_statement = "SELECT * FROM users WHERE email = %s AND hashed_password = %s"
        select_tuple = (email, password)

        return self.executeSelect(select_statement, select_tuple)

    def count_questions(self, job_id):
        cursor = self.__connection.cursor()

        sql = "select count(question) from questions where job_id = '" + \
            str(job_id)+"';"

        cursor.execute(sql)
        num_questions = cursor.fetchone()[0]

        cursor.execute(
            "select question, question_id from questions where job_id = '"+str(job_id)+"';")
        questions = []
        for i in cursor.fetchall():
            questions.append([i[0], i[1]])
        return self.select_questions(num_questions, questions)

    def get_job_title(self, job_id):
        cursor = self.__connection.cursor()
        cursor.execute("select title from jobs where id = '"+str(job_id)+"';")
        job_title = cursor.fetchone()[0]
        return job_title

    def select_questions(self, num, questions):
        numtopick = int(num/2)
        questions_selected = []
        for i in range(numtopick):
            questions_selected.append(questions[randint(0, num-1)])
        return questions_selected

    def create_test(self, job_id, user_id):
        cursor = self.__connection.cursor()
        questions = self.count_questions(job_id)
        sql = "insert into tests values("+str(user_id)+", NULL, False, NULL)"
        cursor.execute(sql)
        self.__connection.commit()
        cursor.execute(
            "select test_id from tests order by test_id desc limit 1")
        id = int(cursor.fetchone()[0])
        # print(id)
        for i in questions:
            sql = "insert into testquestions values(" + \
                str(id)+", "+str(i[1])+")"
            cursor.execute(sql)
        self.__connection.commit()
        questions_json = {}
        for i in questions:
            questions_json["QuestionID"] = i[1]
        return json.dumps(questions_json)

    def score_test(self, answers, test_id):
        cursor = self.__connection.cursor()
        ans = json.loads(answers)
        cursor.execute(
            "select count(question_id) from testquestions where test_id = "+str(test_id))
        num_questions = cursor.fetchone()[0]
        score_q = 100/num_questions
        score = 0
        for i in ans:
            cursor.execute(
                "select correct_answer from questions where question_id = "+str(i["QuestionId"]))
            ans_given = cursor.fetchone()[0]
            if str(ans_given) == str(i["OptionGiven"]):
                score += score_q

        return json.dumps([{'test_id': int(test_id), 'score': float(score)}])

    def get_new_interviews(self):
        cursor = self.__connection.cursor()

        sql = "select * from UserJobs where userjob_id IN (select application_id from feedback where given_feedback = False)"

        cursor.execute(sql)

        return cursor.fetchall()

    def feedback_given(self, application_id, data):
        data = json.loads(data)
        cursor = self.__connection.cursor()

        sql = "update UserJobs set score_degree = "+str(data["Degree"])+", score_alevels = "+str(data["A-Levels"])+", score_lang = "+str(
            data["Languages"])+", score_employment = "+str(data["Employment"])+", score_skills = "+str(data["Skills"])+" where userjob_id = "+str(application_id)

        cursor.execute(sql)
        sql = "update feedback set given_feedback = True where application_id = " + \
            str(application_id)
        cursor.execute(sql)
        self.__connection.commit()

    def get_new_interviews_json(self):
        cursor = self.__connection.cursor()

        sql = "select * from UserJobs where userjob_id IN (select application_id from feedback where given_feedback = False)"

        cursor.execute(sql)

        rows = cursor.fetchall()
        applications = []
        for row in rows:
            user_id = row[0]

            sql = "select name from users where id = "+str(user_id)
            cursor.execute(sql)

            name = cursor.fetchone()[0]
            degree = row[2]
            university = row[3]
            degree_level = row[4]
            a_levels = json.loads(row[5])
            languages = json.loads(row[6])
            employment = json.loads(row[7])
            skills = json.loads(row[8])
            hobbies = json.loads(row[9])
            id = row[19]

            data_send = {"Name": name, "Degree Qualification": degree, "Degree Level": degree_level, "University Attended": university,
                         "A-Level Qualifications": a_levels, "Languages Known": languages, "Previous Employment": employment, "Skills": skills, "Hobbies": hobbies, "ID": id}

            applications.append(data_send)
        json_data = json.dumps(applications)

        return json_data

    def get_applications(self, user_id):
        cursor = self.__connection.cursor()
        sql = "select * from UserJobs where user_id = "+str(user_id)

        cursor.execute(sql)
        row = cursor.fetchall()

        applications = []
        for i in row:
            user_id = i[0]
            sql = "select name from users where id = "+str(user_id)

            cursor.execute(sql)
            name = cursor.fetchone()[0]
            job_id = i[1]

            sql = "select title from jobs where id = "+str(job_id)
            cursor.execute(sql)
            job_title = cursor.fetchone()[0]

            degree = i[2]
            university = i[3]
            degree_level = i[4]
            a_levels = json.loads(i[5])
            languages = json.loads(i[6])
            employment = json.loads(i[7])
            skills = json.loads(i[8])
            hobbies = json.loads(i[9])
            response = i[10]
            feedback = json.loads(i[11])

            application_id = i[19]

            # print(application_id)

            sql = "select given_feedback from feedback where application_id=" + \
                str(application_id)

            cursor.execute(sql)

            # print(cursor.fetchone())
            if cursor.fetchone() == True:
                response = None
                feedback = None

            data_send = {"Name": name, "Degree Qualification": degree, "Degree Level": degree_level, "University Attended": university, "A-Level Qualifications": a_levels,
                         "Languages Known": languages, "Previous Employment": employment, "Skills": skills, "Hobbies": hobbies, "ID": application_id, "Feedback": feedback, "Response": response}

            applications.append(data_send)
        return json.dumps(applications)

    def are_jobs_expired(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        cursor = self.__connection.cursor()
        sql = "update jobs set available = False where CURDATE() > date_expiry"
        cursor.execute(sql)
        self.__connection.commit()

    def get_jobs_available(self):
        self.are_jobs_expired()
        cursor = self.__connection.cursor()
        sql = "select * from jobs where available = True ORDER BY date_posted DESC"
        cursor.execute(sql)

        jobs = []
        for row in cursor.fetchall():
            title = row[0]
            description = row[1]
            responsibilities = row[2]
            people_management = row[3]
            skills_needed = row[4]
            ideal_candidate = row[5]
            education = row[6]
            id = row[7]
            location = row[9]

            data_send = {"ID": id, "Title": title, "Description": description, "Responsibilities": responsibilities, "People Management": people_management,
                         "Skills Needed": skills_needed, "Ideal Candidate": ideal_candidate, "Education": education, "Location": location}
            jobs.append(data_send)

        return json.dumps(jobs)

    def get_jobs_not_available(self):
        self.are_jobs_expired()
        cursor = self.__connection.cursor()
        sql = "select * from jobs where available = False ORDER BY date_posted DESC"
        cursor.execute(sql)

        jobs = []
        for row in cursor.fetchall():
            title = row[0]
            description = row[1]
            responsibilities = row[2]
            people_management = row[3]
            skills_needed = row[4]
            ideal_candidate = row[5]
            education = row[6]
            id = row[7]
            location = row[9]

            data_send = {"ID": id, "Title": title, "Description": description, "Responsibilities": responsibilities, "People Management": people_management,
                         "Skills Needed": skills_needed, "Ideal Candidate": ideal_candidate, "Education": education, "Location": location}
            jobs.append(data_send)

        return json.dumps(jobs)

    def get_jobs(self):
        self.are_jobs_expired()
        cursor = self.__connection.cursor()
        sql = "select * from jobs ORDER BY date_posted DESC"
        cursor.execute(sql)

        jobs = []
        for row in cursor.fetchall():
            title = row[0]
            description = row[1]
            responsibilities = row[2]
            people_management = row[3]
            skills_needed = row[4]
            ideal_candidate = row[5]
            education = row[6]
            id = row[7]
            location = row[9]
            date_posted = str(row[10])
            date_expiry = str(row[11])

            data_send = {"ID": id, "Title": title, "Description": description, "Responsibilities": responsibilities, "People Management": people_management,
                         "Skills Needed": skills_needed, "Ideal Candidate": ideal_candidate, "Education": education, "Location": location, "Date Posted": date_posted, "Date Expiry": date_expiry}
            jobs.append(data_send)

        return json.dumps(jobs)

    def get_jobs_location(self, location):
        self.are_jobs_expired()
        cursor = self.__connection.cursor()
        sql = "select * from jobs where location = '" + \
            str(location)+"' ORDER BY date_posted DESC"
        cursor.execute(sql)
        jobs = []
        for row in cursor.fetchall():
            title = row[0]
            description = row[1]
            responsibilities = row[2]
            people_management = row[3]
            skills_needed = row[4]
            ideal_candidate = row[5]
            education = row[6]
            id = row[7]
            location = row[9]

            data_send = {"ID": id, "Title": title, "Description": description, "Responsibilities": responsibilities, "People Management": people_management,
                         "Skills Needed": skills_needed, "Ideal Candidate": ideal_candidate, "Education": education, "Location": location}
            jobs.append(data_send)

        return json.dumps(jobs)

    def get_locations(self):
        cursor = self.__connection.cursor()
        sql = "select distinct location from jobs"
        cursor.execute(sql)
        locations = []
        for row in cursor.fetchall():
            locations.append(row[0])

        locations_dict = {}

        for i in range(len(locations)):
            locations_dict["Location "+str(i)] = locations[i]

        return json.dumps(locations_dict)

    def create_admin(self, email, password):
        cursor = self.__connection.cursor()

        sql = "select email from admin_users where email = '"+str(email)+"'"

        cursor.execute(sql)

        if cursor.fetchone() != None:
            return False

        sql = "insert into admin_users values('"+str(email)+"', '"+str(password)+"', NULL)"

        cursor.execute(sql)
        self.__connection.commit()
        return True

    def validate_admin(self, email, password):
        cursor = self.__connection.cursor()
        sql = "select email, hashed_password from admin_users where email = '" + str(email)+"'"
        cursor.execute(sql)
        res = cursor.fetchone()
        if res == None:
            return False
        if password == res[1]:
            return True

        return False

    def get_token(self, email, admin):
        cursor = self.__connection.cursor()
        if admin:
            sql = "select id from admin_users where email = '"+str(email)+"'"
        else:
            sql = "select id from users where email = '"+str(email)+"'"
        
        cursor.execute(sql)
        id = cursor.fetchone()[0]

        sql = "select token from tokens where user_id = {0} and is_admin = {1}".format(id, admin)
        cursor.execute(sql)

        return cursor.fetchone()[0]

    def is_admin(self, token):
        cursor = self.__connection.cursor()
        sql = "select is_admin from tokens where token = "+str(token)
        cursor.execute(sql)
        return cursor.fetchone()[0]

    def insert_into_tokens(self, email, token, admin):
        cursor = self.__connection.cursor()
        if admin:
            sql = "select id from admin_users where email = '"+str(email)+"'"
            
        else:
            sql = "select id from users where email = '"+str(email)+"'"
        cursor.execute(sql)
        id = cursor.fetchone()[0]

        sql = "insert into tokens values(NULL, '"+str(token) + \
            "', "+str(id)+", "+str(admin)+")"
        cursor.execute(sql)
        self.__connection.commit()

    def check_key(self, key):
        cursor = self.__connection.cursor()
        sql = "select key_num from key_admin where key_num = "+str(key)
        cursor.execute(sql)

        if cursor.fetchone() == None:
            return False

        return True

    def get_user_id_from_token(self, token):
      cursor = self.__connection.cursor()
      sql = 'select user_id from tokens where token = ' + token
      cursor.excute(sql)
      return cursor.fetchone()[0]
    
