from rest_framework import generics
from ..models import Employee
from ..serializer import EmployeeSerializer

class ActiveEmployeeList(generics.ListAPIView):
    queryset = Employee.objects.filter(active=True)  # Filtra los empleados activos
    serializer_class = EmployeeSerializer
