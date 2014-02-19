__author__ = 'ash'
import mysql.connector



class DatabaseConnection:
    def __init__(self, add="localhost", user="ash", password="5188", db="ACM"):
        self.con = mysql.connector.connect(host=add, user=user, password=password, database=db)
        self.cur = self.con.cursor()

    def exec_query(self, format_str, keys=None):
        if keys is not None:
            # print format_str,keys
            self.cur.execute(format_str, keys)
        else:
            self.cur.execute(format_str)
        return self.cur

    def commit(self):
        self.con.commit()

    def close(self):
        self.con.commit()
        self.con.close()
