from django.db import models
from django.utils import timezone
from .utils import *


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de area', max_length=100, null=False)
    def __str__(self) -> str:
        return '{0}'.format(self.name)
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def undelete(self):
        self.deleted_at = None
        self.save() 

class Employee(models.Model):
    empty_value_display = '- vacio -'
    id = models.AutoField(primary_key=True)
    first_name = models.CharField('Primer Nombre', max_length=100, null=False)
    second_name = models.CharField('Segundo Nombre', max_length=100, null=True)
    last_name = models.CharField('Primer Apellido', max_length=100, null=True)
    second_last_name = models.CharField('Segundo Apellido', max_length=100, null=True)
    identity_card = models.IntegerField('Carnet de Identidad', null=False)
    active = models.BooleanField('Activo',default=True)
    picture = models.ImageField(upload_to=rename_image, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField('Creado en',auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado en ',auto_now=True)

    def __str__(self) -> str:
        return '{0} {1} {2} {3}'.format(self.first_name,self.second_name, self.last_name, self.second_last_name)
        
class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField('Codigo', max_length=100,null=True)
    description = models.CharField('Descripcion', max_length=100, null=True)
    created_at = models.DateTimeField('Creado en',auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado en ',auto_now=True)
    deleted_at = models.DateTimeField('Eliminado en',null=True)
    def __str__(self) -> str:
        return '{1}'.format(self.code, self.description)
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def undelete(self):
        self.deleted_at = None
        self.save()
    
class Evaluation(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return '{0},{1}'.format(self.employee, self. survey)
    
class QuestionManager(models.Manager):
    def detail_question(self, survey_id):
        consulta = self.filter(
        survey_id = survey_id)
        return consulta

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    code = models.CharField('Codigo Pregunta', max_length=100, null=True)
    description = models.CharField('Descripcion', max_length=200)
    image = models.ImageField(upload_to=rename_question_image, null=True)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return '{0}'.format(self.description)

    objects = QuestionManager()

class AnswerOptionManager(models.Manager):
    def detail_answer(self, question_id):
        consultas = self.filter(
            question_id = question_id)
        return consultas

class AnswerOption(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField('Codigo de respuesta', max_length=100, null=True)
    description = models.CharField('Descripcion', max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return '{0},{1}'.format(self.code, self.description)

    objects = AnswerOptionManager()

class Answer(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0},{1},{2}'.format(self.evaluation, self.question, self.answer_option)