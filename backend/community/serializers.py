from rest_framework import serializers
from .models import *

"""
식물일지
"""

class DiaryMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantDiary
        fields = [
            'id',
            'img_url',
            'year',
            'month',
            'day',
            'title'
            ]

class DiaryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantDiary
        fields = [
            'year',
            'month',
            'day',
            'title',
            'pub_date',
            'category',
            'place',
            'sun',
            'water',
            'body',
            'view_cnt'
        ]


class DiaryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantDiary
        fields = [
            'title',
            'plantprofile',
            'category',
            'place',
            'sun',
            'water',
            'year',
            'month',
            'day',
            'img_url',
            'body'
        ]

class DiaryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryImage
        fields = ['diary', 'image', 'body']

class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryImage
        fields = ['plant', 'image', 'body']

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