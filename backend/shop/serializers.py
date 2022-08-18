from rest_framework import serializers
from .models import Plant, PlantImage, Tag

class PlantImageRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'plant_name', 'price']

class PlantRegisterSerializer(serializers.ModelSerializer):
    plant_images=serializers.CharField()
    
    class Meta:
        model = Plant
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'