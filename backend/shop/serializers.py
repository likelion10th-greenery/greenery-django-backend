from rest_framework import serializers
from .models import Plant, PlantImage

class PlantImageRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'plant_name', 'price']

class PlantRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'