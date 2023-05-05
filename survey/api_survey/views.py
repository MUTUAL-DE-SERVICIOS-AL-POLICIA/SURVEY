from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .models import Area
from .serializer import EmployeeSerializer
from .serializer import AreaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
class GetEmployee(APIView):
    def get(self, request, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

class GetArea(APIView):
    def get(self, request, area_id):
        try:
            area = Area.objects.get(id=area_id)
        except Area.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AreaSerializer(area)
        return Response(serializer.data)
    
