import mysql.connector as sql
password=""
con=sql.connect(host="localhost",user="root",passwd=password,database="mcq")
cur=con.cursor()
class SelectUser:
    def select_user_id(self,user_email):
        cur.execute("SELECT user_id FROM user WHERE user_email=%s",(user_email,))
        return cur.fetchone()
    def select_user_passwd(self,user_email):
        cur.execute("SELECT user_password FROM user where user_email=%s",(user_email,))
        return cur.fetchone()
