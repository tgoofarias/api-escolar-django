# Generated by Django 4.1.6 on 2023-02-07 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlunoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CursoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_curso', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
                ('nivel', models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], default='B', max_length=1)),
            ],
        ),
    ]
