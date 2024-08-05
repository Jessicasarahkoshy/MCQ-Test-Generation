from similarity_checker import *
from logging_config import*
from question_db import*
from test_db import*
from test_question_db import*
setup_logging()
logger = logging.getLogger("mcq_generator_service")
question_db_obj=SelectQuestion()
test_db_obj=InsertTest()
test_que_db_obj=InsertTestQue()
class QuestionIsEmptyError(Exception):
    pass
class QuestionIsDigitsError(Exception):
    pass
class QuestionGenerator:
    def __init__(self,user_id,threshold,subject_id,module_list,test_duration,cut_off,marks,no_of_questions):
        self.user_id=user_id
        self.test_duration=test_duration
        self.cut_off=cut_off
        self.threshold=threshold
        self.subject_id=subject_id
        self.module_list=module_list
        self.marks=marks
        self.no_of_questions=no_of_questions
    def question_similarity_checker(self):
        '''This is the main function
              Raise QuestionIsDigitsError:raises an exception when the given question only contains digits
              Raise QuestionIsEmptyError:raises an exception when the given question is empty'''
        question_id=[]
        encoded_question_list=[]
        no_of_questions=0
        total_marks=0
        for module in self.module_list:
            module_id=module["module_id"]
            no_of_questions+=module["no_of_questions"]
            mark=module["mark"]
            id_range=question_db_obj.select_question_id_list(self.subject_id,module_id)
            while(len(question_id)<no_of_questions):
                try:
                    n=random.randrange(len(id_range))
                    qid=id_range[n][0]
                    question=question_db_obj.select_question_by_id(qid)
                    if(question==""):
                        raise QuestionIsEmptyError
                    if(question.isdigit()):
                        raise QuestionIsDigitsError
                except QuestionIsDigitsError:
                    logger.error(f"Question number {n} contains only numbers and therefore is invalid")
                except QuestionIsEmptyError:
                    logger.error(f"Question number {n} is empty")
                else:
                    is_similar_obj=QuestionGeneration(self.threshold,question,encoded_question_list)
                    is_similar_ans=is_similar_obj.is_similar()
                    if(is_similar_ans[0]==True):
                        encoded_question_list.append(is_similar_ans[1])
                        question_id.append({"qid":qid,"mark":mark})
                        logger.info(f"Question {n} added successfully to the list of mcq")
                    else:
                        logger.info(f"Question {n} is not added")
        question_list=[]
        for qid_dict in question_id:
            question=question_db_obj.select_question_and_options(qid_dict["qid"])
            print(question)
            question_dict={"question":question[0],"option1":question[1],"option2":question[2],"option3":question[3],"option4":question[4]}
            question_list.append(question_dict)
        test_id=test_db_obj.insert_test_details(self.user_id,self.subject_id,self.cut_off,self.test_duration,self.marks,self.no_of_questions)
        for qid_dict in question_id:
            test_que_db_obj.insert_que(qid_dict["qid"],test_id,qid_dict["mark"])
        return question_list,test_id
        
