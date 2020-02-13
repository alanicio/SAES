from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.middleware.csrf import get_token
from rest_framework import viewsets
from .serializers import *

def index(request):
    usuarios=User.objects.all()
    data=serializers.serialize('json',usuarios)
    return HttpResponse(data,content_type='application/json')

class PersonaViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows users to be viewed or edited.
    """
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer

		

def store(request):
	llave=request.POST.get('llave')
	return JsonResponse({'llave':llave})

def CSRF_token(request):
	#to do , regresar el token csrf al cliente
	rand_token = uuid4()
	return JsonResponse({"token":rand_token})