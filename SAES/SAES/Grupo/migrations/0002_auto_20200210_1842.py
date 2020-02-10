# Generated by Django 3.0.2 on 2020-02-10 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Grupo', '0001_initial'),
        ('Materia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupomateria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Materia.Materia'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='materia',
            field=models.ManyToManyField(through='Grupo.GrupoMateria', to='Materia.Materia'),
        ),
    ]