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
from openpyxl import Workbook
from django.http import HttpResponse

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

@api_view(['GET'])
def get_survey(request, survey_id):
    try:
        survey = Survey.objects.get(id=survey_id)
        serializer = FormQuestionSerializer(survey)
        return Response(serializer.data)
    except Survey.DoesNotExist:
        return Response(status=404, data={'error': 'Survey not found'})

def get_qualification_report(request):
    try:
        filters = {
        'date_start': request.GET.get('date_start'),
        'date_end': request.GET.get('date_end')
        }
        data_evaluation = Evaluation.objects.get_evaluation_with_answer(**filters)
        wb = Workbook()
        ws = wb.active
        """Creacion del encabezado"""
        headers = ['EMPLEADO','CI','ÁREA', 'CÓDIGO DE FORMULARIO ','DESCRIPCIÓN DEL FORMULARIO','PREGUNTA','RESPUESTA','FECHA']
        ws.append(headers)
        """llenado de datos en hoja de excel"""
        for evaluation in data_evaluation:
            """ Comprueba si cada texto es None antes de concatenarlo"""
            full_name = [texto for texto in [evaluation.employee.first_name, evaluation.employee.second_name, evaluation.employee.last_name, evaluation.employee.second_last_name] if texto is not None]

            """Concatena los componentes de texto con un espacio en blanco entre ellos"""
            full_name = " ".join(full_name)

            """ Recorre las respuestas asociadas a la evaluación"""
            for answer in evaluation.answer_set.all():
                """ Formatear created_at en el formato deseado"""
                created_at_formatted = evaluation.created_at.strftime('%Y-%m-%d %H:%M:%S')
                values = [full_name, evaluation.employee.identity_card, evaluation.employee.area.name, evaluation.survey.code, evaluation.survey.description, answer.question.description, answer.answer_option.description, created_at_formatted]
                ws.append(values)
        """Creación de respuesta para generar el archivo"""
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=datos.xlsx'
        wb.save(response)
        return response
    except Survey.DoesNotExist:
        return Response(status=404, response={'error': 'Survey not found'})