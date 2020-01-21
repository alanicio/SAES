from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
	nombre=models.CharField(max_length=120)
	#carrera=models.ForeignKey(Carrera,on_delete=models.CASCADE)
	encargado=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
