from user_config_db import*
from config import*
from subject_db import*
config_db_obj=SelectConfig()
subject_db_obj=SelectSubject()
def get_test_config_values(user_id):
    config_files=config_db_obj.select_config_by_user_id(user_id)
    test_config_list=[]
    for file in config_files:
        subject_dict={}
        config_values=config(file[0])
        subject_dict["threshold"]=config_values["threshold"]
        subject_id=config_values["subject_id"]
        subject_dict["subject_id"]=subject_id
        module_list=config_values["modules"]
        subject_dict["modules"]=module_list
        subject_dict["test_duration"]=config_values["test_duration"]
        subject_dict["cut_off"]=config_values["cut_off"]
        no_of_questions=0
        marks=0
        for module in module_list:
            marks+=module["no_of_questions"]*module["mark"]
            no_of_questions+=module["no_of_questions"]
        subject_dict["marks"]=marks
        subject_dict["no_of_questions"]=no_of_questions
        subject_dict["subject_name"]=subject_db_obj.select_subject_by_subject_id(subject_id)[0]
        test_config_list.append(subject_dict)
    return test_config_list
