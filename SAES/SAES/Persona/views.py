from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse


def index(request):
    usuarios=User.objects.all()
    data=serializers.serialize('json',usuarios)
    return HttpResponse(data,content_type='application/json')

