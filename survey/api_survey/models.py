from django.db import models
from django.utils import timezone
from .utils import *
from .managers import *


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
    second_name = models.CharField('Segundo Nombre', max_length=100, null=True, blank=True)
    last_name = models.CharField('Primer Apellido', max_length=100, null=True, blank=True)
    second_last_name = models.CharField('Segundo Apellido', max_length=100, null=True, blank=True)
    identity_card = models.IntegerField('Carnet de Identidad', null=False, unique=True)
    active = models.BooleanField('Activo', default=True)
    picture = models.ImageField('Fotografia', upload_to=rename_image, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, verbose_name='Area')
    created_at = models.DateTimeField('Creado en',auto_now_add=True , blank=True)
    updated_at = models.DateTimeField('Actualizado en ',auto_now=True , blank=True)
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    
    def __str__(self) -> str:
        return '{0} {1} {2} {3}'.format(self.first_name,self.second_name, self.last_name, self.second_last_name)

class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField('Codigo', max_length=100,null=True, unique=True)
    description = models.CharField('Descripcion', max_length=100, null=True)
    created_at = models.DateTimeField('Creado en',auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado en ',auto_now=True, blank=True)
    deleted_at = models.DateTimeField('Eliminado en',null=True, blank=True)
    
    class Meta:
        verbose_name = "Encuesta"
        verbose_name_plural = "Encuestas"
        
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
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Empleado')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Encuesta')
    created_at = models.DateTimeField(auto_now_add=True , blank=True)
    updated_at = models.DateTimeField(auto_now=True , blank=True)
    class Meta:
        verbose_name = "Evaluacion"
        verbose_name_plural = "Evaluaciones"
        
    def __str__(self) -> str:
        return '{0},{1}'.format(self.employee, self. survey)
    objects = EvaluationManager()

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Encuesta')
    code = models.CharField('Codigo Pregunta', max_length=100, null=True)
    description = models.CharField('Descripcion', max_length=200)
    state = models.BooleanField('Estado', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
    def __str__(self) -> str:
        return '{0}'.format(self.description)

    objects = QuestionManager()

class AnswerOption(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField('Codigo de respuesta', max_length=100, null=True)
    description = models.CharField('Descripcion', max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Pregunta')
    state = models.BooleanField('Estado', default=True)
    image = models.ImageField(upload_to=rename_question_image, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Opciones de Respuesta"
        verbose_name_plural = "Opciones de Respuestas"
    def __str__(self) -> str:
        return '{0},{1}'.format(self.code, self.description)

    objects = AnswerOptionManager()

class Answer(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, verbose_name='Evaluacion')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Pregunta')
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE,verbose_name='Opcion respondida')
    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
    def __str__(self) -> str:
        return '{0},{1},{2}'.format(self.evaluation, self.question, self.answer_option)
    
class AllowedIps(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.CharField('Direccion Ip', max_length=15, null=False, unique=True)
    owner = models.CharField('Propietario', max_length=100, null=False)
    class Meta:
        verbose_name = "Ip Permitida"
        verbose_name_plural = "Ip's Permitidas"
    def __str__(self) -> str:
        return '{0}'.format(self.ip_address)