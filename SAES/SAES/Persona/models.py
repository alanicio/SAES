from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
	usuario=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	curp=models.CharField(max_length=18)
	fecha_de_nacimiento=models.DateTimeField()
	materia_inscrita=models.ManyToManyField('Grupo.GrupoMateria')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

#class Alumno(object):