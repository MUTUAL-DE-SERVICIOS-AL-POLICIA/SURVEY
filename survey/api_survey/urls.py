from django.urls import path
from .views import EmployeeList
from .views import AreaList

urlpatterns = [
    path('employee/',EmployeeList.as_view(), name = 'employee_list'),
    path('area/',AreaList.as_view(), name = 'area_list'),
]