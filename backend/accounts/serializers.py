from rest_framework import serializers
from .models import *

# 로그인 & 회원가입
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password','password1','phone_num','user_address','user_bool']

# 식물 프로필
class PlantProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantProfile
        fields = '__all__'

class PlantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantProfile
        fields = [
            'id',
            'start_day',
            'nickname',
            'img_url'
        ]

class PlantProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantProfile
        fields = [
            'start_day',
            'nickname',
            'img_url',
            'category',
            'place'
        ]