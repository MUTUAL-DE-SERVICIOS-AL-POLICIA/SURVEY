from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .models import Area
from .serializer import EmployeeSerializer
from .serializer import AreaSerializer

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer