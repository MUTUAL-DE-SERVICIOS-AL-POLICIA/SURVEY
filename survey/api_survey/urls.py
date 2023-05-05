from django.urls import path
from .views import EmployeeList
from .views import AreaList
from .views import GetEmployee
from .views import GetArea

urlpatterns = [
    path('employee/',EmployeeList.as_view(), name = 'employee_list'),
    path('get_employee/<int:employee_id>',GetEmployee.as_view(), name = 'get_employee'),
    path('area/',AreaList.as_view(), name = 'area_list'),
    path('get_area/<int:area_id>',GetArea.as_view(), name = 'get_area'),
]