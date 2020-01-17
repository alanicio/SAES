from django.db import models

class Alumno(models.Model):
	nombre=models.CharField(max_length=150)
	apelllidos=models.CharField(max_length=150)
	num_boleta=models.CharField(max_length=10)
	ingreso=models.DateField()
	fecha_de_nacimientomodels.DateField()
		
