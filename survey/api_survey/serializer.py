from rest_framework import serializers
from .models import Employee
from .models import Area
from .models import Evaluation
from .models import Survey
from .models import Question
from .models import Answer
from .models import AnswerOption

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'identity_card',
            'active',
            'area',
            'picture',
        )
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = (
            'name',
        )
        
class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            'code',
            'description',
        )
        
class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = (
            'employee',
            'survey'
        )
        
class QuestionSerialize(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'survey',
            'code',
            'description',
            'state',
            'image',
        )
        
class AnswerSerialize(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'evaluation',
            'question',
            'answer_option',
        )
        
class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = (
            'id',
            'code',
            'description',
            'question',
            'state',
        )
class FormQuestionSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    class Meta:
        model = Survey
        fields = (
            'id',
            'code',
            'description',
            'questions')
    def get_questions(self,obj):
        query = Question.objects.detail_question(obj.id)
        detail_question_answer = DetailQuestionAnswerSerializer(query,many=True).data
        return detail_question_answer

class DetailQuestionAnswerSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields =(
            'id',
            'code',
            'description',
            'state',
            'image',
            'answers'
        )
    def get_answers(self,obj):
         query = AnswerOption.objects.detail_answer(obj.id)
         answer_option = AnswerOptionSerializer(query,many=True).data
         return answer_option
