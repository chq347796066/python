import pymysql


class mysql_util:
    @staticmethod
    def get_connect():
        db = pymysql.connect("localhost", "root", "root", "py_db")
        cursor = db.cursor()
        return cursor

    @staticmethod
    def execute(cursor,sql):
        cursor.execute(sql)

    @staticmethod
    def close(cursor):
        cursor.close()



