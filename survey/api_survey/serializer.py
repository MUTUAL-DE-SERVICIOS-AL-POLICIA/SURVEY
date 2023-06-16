from rest_framework import serializers
from .models import Employee
from .models import Area
from .models import Evaluation
from .models import Survey
from .models import Question
from .models import Answer
from .models import AnswerOption
import base64

class EmployeeSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'identity_card',
            'active',
            'area',
            'picture',
        )

    def get_picture(self, obj):
        if obj.picture:
            with open(obj.picture.path, 'rb') as f:
                encoded_image = base64.b64encode(f.read())
                return encoded_image.decode('utf-8')
        else:
            return None

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        picture = self.get_picture(instance)
        if picture is not None:
            ret['picture'] = f"data:image/png;base64,{picture}"
        return ret
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = (
            'id',
            'name',
        )
        
class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            'id',
            'code',
            'description',
        )
        
class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = (
            'id',
            'employee',
            'survey'
        )
        
class QuestionSerialize(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'survey',
            'code',
            'description',
            'state',
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
            'image',
        )
        
    def get_image(self, obj):
        if obj.image:
            with open(obj.image.path, 'rb') as f:
                encoded_image = base64.b64encode(f.read())
                return encoded_image.decode('utf-8')
        else:
            return None

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        picture = self.get_image(instance)
        if picture is not None:
            ret['picture'] = f"data:image/png;base64,{picture}"
        return ret
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
            'answers'
        )
    def get_answers(self,obj):
         query = AnswerOption.objects.detail_answer(obj.id).order_by('code')
         answer_option = AnswerOptionSerializer(query,many=True).data
         return answer_option
