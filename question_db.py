import mysql.connector as sql
password=""
con=sql.connect(host="localhost",user="root",passwd=password,database="mcq")
cur=con.cursor()
class SelectQuestion:
    def select_question_id_list(self,subject_id,module_id):
        cur.execute("SELECT question_id from question where subject_id=%s and module_id=%s",(subject_id,module_id))
        return cur.fetchall()
    def select_question_by_id(self,question_id):
        cur.execute("SELECT question from question where question_id=%s",(question_id,))
        return cur.fetchone()[0]
    def select_question_and_options(self,question_id):
        cur.execute("SELECT question,option_1,option_2,option_3,option_4 from question where question_id=%s",(question_id,))
        return cur.fetchone()
    def select_question_ans_by_qid(self,question_id):
         cur.execute("SELECT  correct_answer from question where question_id=%s",(question_id,))
         return cur.fetchone()
