from rest_framework import serializers
from .models import Plant, PlantImage

class PlantRegisterSerializer(serializers.ModelSerializer): # 판매자가 식물을 register할 때 이용
    class Meta:
        model = Plant
        fields = [
            'feed_title',
            'plant_name',
            'category',
            'price',
            'stock',
            'shop_tags',
            'origin',
            'plant_width',
            'plant_vertical',
            'plant_height',
            'pot_type',
            'deliver_type',
            'address',
            'plant_detail'
        ]

class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ['plant', 'image']

class PlantSerializer(serializers.ModelSerializer): # 메인화면에서 보이는 이미지
    class Meta:
        model = Plant
        fields = ['pub_date', 'view_cnt', 'id', 'img_url', 'img_cnt', 'plant_name', 'feed_title', 'price']

class PlantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = [
            'id',
            'pub_date',
            'view_cnt',

            'category',
            'plant_name',
            'feed_title', # 게시글 제목 = 제품 한 줄 소개
            'shop_tags',
            'price',
            # 배송비,
            'origin',
            'deliver_type',
            'address',
            'plant_width',
            'plant_vertical',
            'plant_height',
            'stock',
            # 판매자 이름
        ]