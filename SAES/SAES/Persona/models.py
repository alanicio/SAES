from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
	usuario=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	curp=models.CharField(max_length=18)
	fecha_de_nacimiento=models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Alumno(models.Model):
	datos_personales=models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
	boleta=models.CharField(max_length=10)
	materia_inscrita=models.ManyToManyField('Grupo.GrupoMateria',through='Materia.MateriaInscrita')
