
import pymysql

from db.mysql_util import mysql_util

def mysql_test01():
    cursor = mysql_util.get_connect()
    cursor.execute("SELECT VERSION()")
    data=cursor.fetchone()
    print("Database version: %s"% data)
    cursor.close()

def mysql_test02():
    cursor= mysql_util.get_connect()
    sql="""CREATE TABLE IF NOT EXISTS EMPLOYEE  (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
    cursor.execute(sql)
    cursor.close()

def mysql_test03():
    db = pymysql.connect("localhost", "root", "root", "py_db")
    cursor = db.cursor()
    sql="""
    INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)
    """
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        print("add success")

def mysql_test03():
    db = pymysql.connect("localhost", "root", "root", "py_db")
    cursor = db.cursor()
    sql = """
            SELECT * FROM EMPLOYEE
            """
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))

def add_data():
    db = pymysql.connect("localhost", "root", "root", "py_db")
    cursor = db.cursor()
    for i in range(10):
        sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ( %s,%s,%s,%s,%s)" % ("'make"+str(i)+"'","'chen"+str(i)+"'",29,"'N'",2000)
        print(sql)
        cursor.execute(sql)
        db.commit()
    cursor.close()


if __name__=='__main__':
    mysql_test03()



