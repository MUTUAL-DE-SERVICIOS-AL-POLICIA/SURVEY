# Generated by Django 4.2.1 on 2023-05-22 21:14

import api_survey.utils
from django.db import migrations, models
import django.db.models.deletion

def create_initial_data(apps, schema_editor):
        allowed_ips = apps.get_model('api_survey', 'AllowedIps')
        allowed_ips.objects.create(ip_address = '127.0.0.1', owner = 'Administrador')
class Migration(migrations.Migration):

    initial = True
        
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedIps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=15, unique=True, verbose_name='ip')),
                ('owner', models.CharField(max_length=100, verbose_name='Propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de area')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='Primer Nombre')),
                ('second_name', models.CharField(max_length=100, null=True, verbose_name='Segundo Nombre')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Primer Apellido')),
                ('second_last_name', models.CharField(max_length=100, null=True, verbose_name='Segundo Apellido')),
                ('identity_card', models.IntegerField(unique=True, verbose_name='Carnet de Identidad')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('picture', models.ImageField(null=True, upload_to=api_survey.utils.rename_image)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado en ')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_survey.area')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100, null=True, unique=True, verbose_name='Codigo')),
                ('description', models.CharField(max_length=100, null=True, verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado en ')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Eliminado en')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100, null=True, verbose_name='Codigo Pregunta')),
                ('description', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('state', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_survey.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_survey.employee')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_survey.survey')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100, null=True, verbose_name='Codigo de respuesta')),
                ('description', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('state', models.BooleanField(default=True)),
                ('image', models.ImageField(null=True, upload_to=api_survey.utils.rename_question_image)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_survey.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_survey.answeroption')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_survey.evaluation')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_survey.question')),
            ],
        ),
        
        migrations.RunPython(create_initial_data),
    ]
