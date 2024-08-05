from test_question_db import*
from question_db import*
from test_db import*
question_db_obj=SelectQuestion()
test_obj=InsertTestQue()
test_db_obj=InsertTest()
class ScoreCalculation():
    def score_calculation(self,test_id,ans_list):
        qid_list=test_obj.select_qid_by_test_id(test_id)
        for i in range(0,len(qid_list)):
            test_obj.insert_option(test_id,qid_list[i][0],ans_list[i])
        correct_ans=[]
        for qid in qid_list:
            ans=question_db_obj.select_question_ans_by_qid(qid[0])
            correct_ans.append(ans[0])
        scored_marks=0
        for i in range(0,len(qid_list)):
            if(correct_ans[i]==ans_list[i]):
                scored_marks+=10
        cut_off=test_db_obj.select_cut_off(test_id)
        test_db_obj.insert_scored_marks(scored_marks,test_id)
        return {"marks":scored_marks,"cut_off":cut_off[0]}
        
