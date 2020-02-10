# Generated by Django 3.0.2 on 2020-02-07 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grupo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('lunes', models.CharField(max_length=11)),
                ('martes', models.CharField(max_length=11)),
                ('miercoles', models.CharField(max_length=11)),
                ('jueves', models.CharField(max_length=11)),
                ('viernes', models.CharField(max_length=11)),
                ('sabado', models.CharField(max_length=11)),
                ('domingo', models.CharField(max_length=11)),
                ('curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Grupo.GrupoMateria')),
            ],
        ),
    ]