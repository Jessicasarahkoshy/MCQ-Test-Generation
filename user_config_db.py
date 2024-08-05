import mysql.connector as sql
password=""
con=sql.connect(host="localhost",user="root",passwd=password,database="mcq")
cur=con.cursor()
class SelectConfig:
    def select_config_by_user_id(self,user_id):
        cur.execute("SELECT config_file FROM user_config_map WHERE user_id=%s",(user_id,))
        return cur.fetchall()

