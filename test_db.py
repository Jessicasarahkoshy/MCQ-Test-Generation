import mysql.connector as sql
password=""
con=sql.connect(host="localhost",user="root",passwd=password,database="mcq")
cur=con.cursor()
class InsertTest:
    def insert_test_details(self,user_id,subject_id,cut_off,test_duration,total_marks,no_of_questions):
        cur.execute("INSERT INTO test(user_id,subject_id,cut_off,max_test_duration,total_mark,total_number_of_questions) VALUES(%s,%s,%s,%s,%s,%s)",(user_id,subject_id,cut_off,test_duration,total_marks,no_of_questions))
        con.commit()
        cur.execute("SELECT test_id FROM test WHERE user_id=%s",(user_id,))
        res=cur.fetchall()
        test_id=res[len(res)-1][0]
        return test_id
    def select_cut_off(self,test_id):
        cur.execute("SELECT cut_off FROM test WHERE test_id=%s",(test_id,))
        return cur.fetchone()
    def insert_scored_marks(self,scored_marks,test_id):
        cur.execute("UPDATE test SET scored_mark=%s WHERE test_id=%s",(scored_marks,test_id))
        con.commit()
