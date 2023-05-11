from django.db import models

class QuestionManager(models.Manager):
    def detail_question(self, survey_id):
        questions = self.filter(
        survey_id = survey_id).exclude(state=False)
        return questions

class AnswerOptionManager(models.Manager):
    def detail_answer(self, question_id):
        answer_options = self.filter(
        question_id = question_id).exclude(state=False)
        return answer_options

