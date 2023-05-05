from django.shortcuts import render
from api_survey.models import *
from rest_framework import viewsets
from api_survey.serializer import *

class EmployeeTask(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class AreaTask(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer    

class EvaluationTask(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    
class SurveyTask(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer