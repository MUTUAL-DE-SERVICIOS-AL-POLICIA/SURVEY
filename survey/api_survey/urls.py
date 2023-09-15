from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from api_survey.views.modelsviews import *
from api_survey.views.surveyviews import *
from api_survey.views.employeeviews import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView,)

router_employee = router_area = router_evaluation = router_survey = router_question = router_answer_option = router_answer = router_get_survey = DefaultRouter()
router_employee.register(r'employee', EmployeeTask, basename="Empleados")
router_area.register(r'area', AreaTask, basename="areas")
router_evaluation.register(r'evaluation', EvaluationTask, basename="Evaluaciones")
router_survey.register(r'survey', SurveyTask, basename="Encuestas")
router_question.register(r'question', QuestionsTask, basename="preguntas")
router_answer_option.register(r'answer_option', AnswerOptionTask, basename="Opciones de respuesta")
router_answer.register(r'answer', AnswerTask, basename="Respuesta")

urlpatterns = [
    path('', include(router_employee.urls)),
    path('', include(router_area.urls)),
    path('', include(router_evaluation.urls)),
    path('', include(router_survey.urls)),
    path('', include(router_answer_option.urls)),
    path('', include(router_answer.urls)),
    path('save_evaluation',save_evaluation, name='save_evaluation'),
    path('get_survey/<int:survey_id>/answers',get_survey, name='get_survey'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('get_qualification_report/excel/', get_qualification_report, name='get_qualification_report'),
    path('employee_active/', ActiveEmployeeList.as_view(), name='active-employees-list'),
]