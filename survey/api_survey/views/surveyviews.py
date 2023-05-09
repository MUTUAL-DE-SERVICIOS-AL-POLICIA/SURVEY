
from django.shortcuts import render
from api_survey.models import *
from rest_framework.response import Response
from api_survey.serializer import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.db import transaction

@csrf_exempt
@transaction.atomic()
def save_evaluation(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            if not Employee.objects.filter(id=data['employee_id']).exists():
                raise ValidationError('Empleado inexistente')
            if not Survey.objects.filter(id=data['survey_id']).exists():
                raise ValidationError('Encuesta inexistente')
            evaluation = Evaluation.objects.create(employee_id=data['employee_id'], survey_id = data['survey_id'])
            evaluation.save()
            answers = data['answers']
            for answer in answers:
                if not Question.objects.filter(id=answer['question_id']).exists():
                    raise ValidationError('Pregunta inexistente')
                if not AnswerOption.objects.filter(id=answer['answer_option_id']).exists():
                    raise ValidationError('Respuesta inexistente')
                answer = Answer.objects.create(evaluation_id = evaluation.id, question_id = answer['question_id'], answer_option_id = answer['answer_option_id'])
                answer.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
    except Evaluation.DoesNotExist:
         return Response(status=404, data={'error': 'Evaluation not found'})
        
        

