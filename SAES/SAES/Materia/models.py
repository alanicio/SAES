from django.db import models

class Materia(models.Model):
	nombre=models.CharField(max_length=120)
	creditos=models.DecimalField(max_digits=2,decimal_places=2)
	nivel=models.PositiveSmallIntegerField()
	departamento=models.ForeignKey('Departamento.Departamento',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

# MateriaInscrita son los datos individuales de los alumnos con su materia
class MateriaInscrita(models.Model):
	alumno=models.ForeignKey('Persona.Alumno',on_delete=models.CASCADE)
	grupo_materia=models.ForeignKey('Grupo.GrupoMateria',on_delete=models.CASCADE)
	periodo=models.CharField(max_length=7)
	fecha_inscrita=models.DateTimeField(auto_now_add=True)
	aprobada=models.BooleanField(null=True)
	# Si aprobada es:
	# 	null=Se esta cursando
	# 	false=Se reprobo
	#	true=Ya se curso y aprobo

class Calificaciones(models.Model):
	materia=models.ForeignKey(MateriaInscrita,on_delete=models.CASCADE)
	primer_parcial=models.PositiveSmallIntegerField()
	segundo_parcial=models.PositiveSmallIntegerField()
	tercer_parcial=models.PositiveSmallIntegerField()
	final=models.PositiveSmallIntegerField()
	extraordinario=models.PositiveSmallIntegerField(null=True)
	ets=models.PositiveSmallIntegerField(null=True)
