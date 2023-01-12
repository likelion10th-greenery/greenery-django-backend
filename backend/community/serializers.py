from rest_framework import serializers
from .models import *

"""
식물일지
"""

class PlantPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantDiary
        fields = [
            'title', 
            'username',  
            'order', 
            'category', 
            'place', 
            'plant_tags', 
            'post_img',
            'img_url', 
            'pub_date'
            ]

"""
질의응답
"""

class QnAMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = [
            'id',
            'pub_date',
            'title',
            'body',
            # 작성자 이름
            'view_cnt',
            # 좋아요
            # 댓글
            'img_url',
            'img_cnt'
        ]

class QnADetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = [
            'title',
            'body',
            'qna_tags',
            # 좋아요
            # 책갈피
            'view_cnt',
            # 작성자 프로필
            # 댓글
        ]

class QnAPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = [
            'title',
            'body',
            'qna_tags',
        ]

class QnAImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnAImage
        fields = ['qna', 'image']