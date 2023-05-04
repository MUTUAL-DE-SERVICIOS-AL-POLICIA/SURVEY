from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'identity_card',
        )