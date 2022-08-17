from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'pic1', 'plant_name', 'price']

class PlantRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

