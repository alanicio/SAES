from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Persona
		fields = '__all__'