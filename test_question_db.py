import mysql.connector as sql
password=""
con=sql.connect(host="localhost",user="root",passwd=password,database="mcq")
cur=con.cursor()
class InsertTestQue:
    def insert_que(self,q_id,test_id,mark):
        cur.execute("INSERT INTO test_question_map(test_id,question_id,mark) VALUES(%s,%s,%s)",(test_id,q_id,mark))
        con.commit()
    def select_qid_by_test_id(self,test_id):
        cur.execute("SELECT question_id from test_question_map WHERE test_id=%s",(test_id,))
        return cur.fetchall()
    def insert_option(self,test_id,qid,option):
        cur.execute("UPDATE test_question_map SET option_selected=%s WHERE test_id=%s AND question_id=%s",(option,test_id,qid))
        con.commit()
