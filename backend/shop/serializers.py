from rest_framework import serializers
from .models import Plant, Tag

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'pic1', 'plant_name', 'price']

class PlantRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'