import sentence_transformers
import random
import numpy as np
class QuestionGeneration:
    def __init__(self,threshold,question,encoded_question_list):
        '''This is the constructor for the class QuestionGeneration
              param1:threshold-threshold value of similarity between the questions selected
              param2:question-random question that is used to check for similarity with already selected questions
              param3:encoded_question_list-list of questions selected'''
        self.threshold=threshold
        self.question=question
        self.encoded_question_list=encoded_question_list
    def is_similar(self):
        '''This function is used to find if the given string is similar to the given list of strings or not
              return:The function returns true if the question is not similar to the given list of strings and false if it is similar.
              Encoded is returned with the boolean value.'''
        if (self.encoded_question_list==[]):
            encoded_question=self.question_encoding_func(self.question)
            return(True,encoded_question)
        else:
            encoded_question=self.question_encoding_func(self.question)
            score=self.top_score(encoded_question,self.encoded_question_list)
            if(score[0][0]["score"]<self.threshold):
                return(True,encoded_question)
            else:
                return(False,encoded_question)
                
    def question_encoding_func(self,question):
        '''This function is used for encoding,using sentence_transformer.
              param1:question-question that needs to be encoded.
              return:encoded_question'''
        model = sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2')
        encoded_question=model.encode(question)
        return encoded_question
    def top_score(self,encoded_question,encoded_question_list):
        '''This function is used to calculate the most similarity score between the question and the selected question list'''
        score=sentence_transformers.util.semantic_search(encoded_question,np.array(encoded_question_list),top_k=1)
        return score
