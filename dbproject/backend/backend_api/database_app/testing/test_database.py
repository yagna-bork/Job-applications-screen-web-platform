import mysql.connector
import pytest

db = None

db = mysql.connector.connect(
host="localhost",
user="root",
passwd="caramel",
database="TEST"
)

def test_insert():
    cursor = db.cursor()
    sql = "SET FOREIGN_KEY_CHECKS = 0"
    cursor.execute(sql)
    sql = "Truncate table users"
    cursor.execute(sql)
    sql = "Truncate table jobs"
    cursor.execute(sql)
    sql = "Truncate table UserJobs"
    cursor.execute(sql)
    sql = "Truncate table feedback"
    cursor.execute(sql)
    sql = "Truncate table questions"
    cursor.execute(sql)
    sql = "Truncate table tests"
    cursor.execute(sql)
    sql = "Truncate table testquestions"
    cursor.execute(sql)
    sql = "Truncate table testdata"
    cursor.execute(sql)
    sql = "SET FOREIGN_KEY_CHECKS = 1"
    cursor.execute(sql)
    db.commit()
    sql = "INSERT INTO users values('Nathan Bailey', 'nathanbaileyw@gmail.com', 'x', NULL)"
    cursor.execute(sql)
    db.commit()
    sql = "INSERT INTO jobs values('title', 'x', 'x', 'x', 'x', 'x', 'x', NULL, true, 'x');"
    cursor.execute(sql)
    db.commit()
    sql = "insert into UserJobs values(1, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3, 4, 5, 6, 7, false,  NULL);"
    cursor.execute(sql)
    db.commit()
    sql = "insert into testdata values(NULL, 2.3, 2.5, 1.7, 3.7, 7.0, 3);"
    cursor.execute(sql)
    db.commit()
    sql = "insert into questions values('hi', NULL, 1, 'x', 'x', 'x', 'x', 'd');"
    cursor.execute(sql)
    db.commit()
    sql = "insert into questions values('hi', NULL, 1, 'x', 'x', 'x', 'x', 'a');"
    cursor.execute(sql)
    db.commit()
    sql = "insert into questions values('hi', NULL, 1, 'x', 'x', 'x', 'x', 'b');"
    cursor.execute(sql)
    db.commit()
    sql = "insert into tests values(1, 100, true, NULL);"
    cursor.execute(sql)
    db.commit()
    sql = "insert into testquestions values(1, 1);"
    cursor.execute(sql)
    db.commit()

def test_select():
    cursor = db.cursor()
    cursor.execute("select * from users")
    cursor.fetchall()
    cursor.execute("select * from jobs")
    cursor.fetchall()
    cursor.execute("select * from UserJobs")
    cursor.fetchall()
    cursor.execute("select * from testdata")
    cursor.fetchall()
    cursor.execute("select * from questions")
    cursor.fetchall()
    cursor.execute("select * from tests")
    cursor.fetchall()
    cursor.execute("select * from testquestions")
    cursor.fetchall()


    cursor.close()
    db.close()





