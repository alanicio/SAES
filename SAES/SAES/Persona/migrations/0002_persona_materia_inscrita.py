# Generated by Django 3.0.2 on 2020-02-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grupo', '0001_initial'),
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='materia_inscrita',
            field=models.ManyToManyField(to='Grupo.GrupoMateria'),
        ),
    ]