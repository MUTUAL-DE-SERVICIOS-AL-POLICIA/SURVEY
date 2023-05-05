from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from api_survey.views.modelsviews import EmployeeTask
from api_survey.views.modelsviews import AreaTask
from api_survey.views.modelsviews import EvaluationTask
from api_survey.views.modelsviews import SurveyTask

router_employee = DefaultRouter()
router_employee.register(r'employee', EmployeeTask, basename="employees")
router_area = DefaultRouter()
router_area.register(r'area', AreaTask, basename="areas")
router_evaluation = DefaultRouter()
router_evaluation.register(r'evaluation', EvaluationTask, basename="evaluations")
router_survey = DefaultRouter()
router_survey.register(r'survey', SurveyTask, basename="encuestas")

urlpatterns = [
    path('', include(router_employee.urls)),
    path('', include(router_area.urls)),
    path('', include(router_evaluation.urls)),
    path('', include(router_survey.urls)),
]