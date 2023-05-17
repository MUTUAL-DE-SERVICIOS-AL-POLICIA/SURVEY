from time import timezone
from django.db import models
from django.db.models import Prefetch

from datetime import date



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
class EvaluationManager(models.Manager):
    def get_evaluation_with_answer(self,**filters):
        if not filters['date_start']:
            filters['date_start'] = date.today()
        if not filters['date_end']:
            filters['date_end'] = date.today()
        evaluation_data = self.prefetch_related('employee', 'survey', 'employee__area', 'answer_set','answer_set__question','answer_set__answer_option').filter(created_at__date__range =(filters['date_start'], filters['date_end'])).all()
        return evaluation_data

