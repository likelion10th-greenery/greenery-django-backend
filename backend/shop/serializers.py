from rest_framework import serializers
from .models import Plant, PlantImage, Tag

class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer): # 구매자가 shop main에서 볼 때 이용
    class Meta:
        model = Plant
        fields = ['id', 'feed_title', 'plant_type', 'price', 'img_url']


class PlantRegisterSerializer(serializers.ModelSerializer): # 판매자가 식물을 register할 때 이용
    class Meta:
        model = Plant
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']