# Generated by Django 3.0.3 on 2020-02-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Materia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateriaInscrita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]