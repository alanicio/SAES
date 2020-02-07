from django.db import models

class Grupo(models.Model):
	nombre=models.CharField(max_length=5)
	turno=models.CharField(max_length=11,blank=True,null=True,)
	materia=models.ManyToManyField('Materia.Materia', through='GrupoMateria')

class GrupoMateria(models.Model):
	grupo=models.ForeignKey(Grupo,on_delete=models.CASCADE)
	materia=models.ForeignKey('Materia.Materia',on_delete=models.CASCADE)
	inscritos=models.PositiveSmallIntegerField()