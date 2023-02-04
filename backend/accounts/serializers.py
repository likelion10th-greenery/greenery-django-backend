from rest_framework import serializers
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password','password1','phone_num','user_address','user_bool','nickname','introduction','instagram_id','youtube_id','blog_id','profile_img']