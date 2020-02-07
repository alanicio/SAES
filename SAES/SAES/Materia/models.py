from django.db import models

class Materia(models.Model):
	nombre=models.CharField(max_length=120)
	creditos=models.DecimalField(max_digits=2,decimal_places=2)
	nivel=models.PositiveSmallIntegerField()
	departamento=models.ForeignKey('Departamento.Departamento',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
