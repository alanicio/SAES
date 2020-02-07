from django.db import models

class Grupo(models.Model):
	nombre=models.CharField(max_length=5)
	turno=models.CharField(max_length=11,blank=True,null=True,)
	materia=models.ManyToManyField('Materia.Materia', through='GrupoMateria')

class GrupoMateria(models.Model):
	grupo=models.ForeignKey(Grupo,on_delete=models.CASCADE)
	materia=models.ForeignKey('Materia.Materia',on_delete=models.CASCADE)
	inscritos=models.PositiveSmallIntegerField()

class Horario(models.Model):
	lunes=models.CharField(max_length=11)
	martes=models.CharField(max_length=11)
	miercoles=models.CharField(max_length=11)
	jueves=models.CharField(max_length=11)
	viernes=models.CharField(max_length=11)
	sabado=models.CharField(max_length=11)
	domingo=models.CharField(max_length=11)
	curso=models.OneToOneField(GrupoMateria,on_delete=models.CASCADE,primary_key=True)