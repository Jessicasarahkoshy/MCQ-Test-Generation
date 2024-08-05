from flask import Flask, request,jsonify
from flask_cors import CORS
from mcq_generator_service import *
from user_test_display_service import*
from mcq_generator_service import *
from user_db import*
from test_score_service import*
from logging_config import*
setup_logging()
logger = logging.getLogger("user_test_display_app")
class ThresholdNotProvidedError(Exception):
    pass
class ThresholdNotIntError(Exception):
    pass
class SubjectIdNotProvidedError(Exception):
    pass
class SubjectIdNotIntError(Exception):
    pass
class CutOffNotIntError(Exception):
    pass
class ModulesInfoNotProvidedError(Exception):
    pass
class TestDurationNotProvidedError(Exception):
    pass
class CutOffNotProvidedError(Exception):
    pass
class UserIdNotProvidedError(Exception):
    pass
class UserIdNotIntError(Exception):
    pass
class MarksNotProvidedError(Exception):
    pass
class MarksNotIntError(Exception):
    pass
class NoOfQuestionsNotProvidedError(Exception):
    pass
class NoOfQuestionsNotIntError(Exception):
    pass
user_db_obj=SelectUser()
test_score_obj=ScoreCalculation()
app = Flask(__name__)
CORS(app)
@app.route("/mcqtest/user", methods=['POST'])
def user_config():
        data=request.get_json()
        user_email=data.get("user_email")
        user_passwd=data.get("user_passwd")
        user_id=user_db_obj.select_user_id(user_email)
        if(user_id==None):
            response={"message":"email doesnt exist"}
            return jsonify(response)
        passwd=user_db_obj.select_user_passwd(user_email)
        if(user_passwd!=passwd[0]):
            response={"message":"incorrect password"}
            return jsonify(response)
        test_configs=get_test_config_values(user_id[0])
        response={"message":"True","test_configs": test_configs,"user_id":user_id}
        return jsonify(response)
@app.route("/mcqtest/test", methods=['POST'])
def mcq_test():
        '''This is used to get the questions'''
        data=request.get_json()
        try:
            threshold=data.get("threshold")
            if(threshold==None):
                raise ThresholdNotProvidedError
            if(type(threshold) is not float):
                raise ThresholdNotIntError
        except ThresholdNotProvidedError:
            logger.error("Threshold is not provided.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        except ThresholdNotIntError:
            logger.error("Given threshold is not an integer.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        try:
            subject_id=data.get("subject_id")
            if(subject_id==None):
                raise SubjectIdNotProvidedError
            if(type(subject_id) is not int):
                raise SubjectIdNotIntError
        except SubjectIdNotProvidedError:
            logger.error("subject_id is not provided.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        except SubjectIdNotIntError:
            logger.error("Given subject_id is not an integer.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        try:
            module_list=data.get("modules")
            if(module_list==None):
                raise ModulesInfoNotProvidedError
        except ModulesInfoNotProvidedError:
            logger.error("Information of modules is not provided")
            return {"message":"Internal server error.please try again later."}
        try:
            test_duration=data.get("test_duration")
            if(test_duration==None):
                raise TestDurationNotProvidedError
        except TestDurationNotProvidedError:
            logger.error("Test Duration is not provided")
            return {"message":"Internal server error.please try again later."}
        try:
            cut_off=data.get("cut_off")
            if(cut_off==None):
                raise CutOffNotProvidedError
            if(type(cut_off) is not int):
                raise CutOffNotIntError
        except CutOffNotProvidedError:
            logger.error("cut_off is not provided.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        except CutOffNotIntError:
            logger.error("Given cut_off is not an integer.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        try:
            user_id=data.get("user_id")
            if(user_id==None):
                raise UserIdNotProvidedError
            if(type(user_id) is not int):
                raise UserIdNotIntError
        except UserIdNotProvidedError:
            logger.error("user_id is not provided.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        except UserIdNotIntError:
            logger.error("Given user_id is not an integer.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        try:
            marks=data.get("marks")
            if(marks==None):
                raise MarksNotProvidedError
            if(type(marks) is not int):
                raise MarksNotIntError
        except MarksNotProvidedError:
            logger.error("marks is not provided.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        except MarksNotIntError:
            logger.error("Given marks is not an integer.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        try:
            no_of_questions=data.get("no_of_questions")
            if(no_of_questions==None):
                raise NoOfQuestionsNotProvidedError
            if(type(no_of_questions) is not int):
                raise NoOfQuestionsNotIntError
        except NoOfQuestionsNotProvidedError:
            logger.error("no_of_questions is not provided.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        except NoOfQuestionsNotIntError:
            logger.error("Given no_of_questions is not an integer.Please provide a integer number.")
            return {"message":"Internal server error.please try again later."}
        mcq_generator_obj=QuestionGenerator(user_id,threshold,subject_id,module_list,test_duration,cut_off,marks,no_of_questions)
        question_list,test_id=mcq_generator_obj.question_similarity_checker()
        response={"message":"success","question_list":question_list,"test_id":test_id}
        return jsonify(response)
@app.route("/mcqtest/score", methods=['POST'])
def test_score():
    data=request.get_json()
    test_id=data.get("test_id")
    ans_list=data.get("answer_list")
    response=test_score_obj.score_calculation(test_id,ans_list)
    return jsonify(response)
if __name__=="__main__":
    app.run()
