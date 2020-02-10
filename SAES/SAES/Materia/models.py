from django.db import models

class Materia(models.Model):
	nombre=models.CharField(max_length=120)
	creditos=models.DecimalField(max_digits=2,decimal_places=2)
	nivel=models.PositiveSmallIntegerField()
	departamento=models.ForeignKey('Departamento.Departamento',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class MateriaInscrita(models.Model):
	alumno=models.ForeignKey('Persona.Alumno',on_delete=models.CASCADE)
	grupo_materia=models.ForeignKey('Grupo.GrupoMateria',on_delete=models.CASCADE)
	

	
		