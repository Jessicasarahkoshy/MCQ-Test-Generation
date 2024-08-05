import mysql.connector as sql
password=""
con=sql.connect(host="localhost",user="root",passwd=password,database="mcq")
cur=con.cursor()
class SelectSubject:
    def select_subject_by_subject_id(self,subject_id):
        cur.execute("SELECT subject_name FROM subject WHERE subject_id=%s",(subject_id,))
        return cur.fetchone()
