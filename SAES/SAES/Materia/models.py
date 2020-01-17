from django.db import models

class Materia(models.Model):
	nombre=models.CharField(max_length(120))
	creditos=models.DecimalField(max_digits=2,decimal_places=2)
	nivel=models.PositiveSmallIntegerField()
		
