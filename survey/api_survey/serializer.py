from rest_framework import serializers
from .models import Employee
from .models import Area

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
            'active',
            'area_id',
        )
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = (
            'name',
        )