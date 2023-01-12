from rest_framework import serializers
from .models import *

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeSharing
        fields = [
            "pub_date",
            "dealtype",
            "dealstate",
            "dealitem",
            "sharing_feed_title",
            "item",
            "img_url",
            "img_cnt",
            "exchange_method",
            "communicate_method",
            "add_text",
            "sharing_tags",
            "view_cnt",
            # 좋아요
            # 책갈피
            # 작성자 프로필
            # 댓글
        ]

class SharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeSharing
        fields = [
            "pub_date",
            "dealtype",
            "dealstate",
            "dealitem",
            "sharing_feed_title",
            "item",
            "img_url",
            "img_cnt",
            "sharing_method",
            "selection_method",
            "notice_date",
            "add_text",
            "sharing_tags",
            "view_cnt",
            # 좋아요
            # 책갈피
            # 작성자 프로필
            # 댓글
        ]

class GetAll(serializers.ModelSerializer):
    class Meta:
        model = ExchangeSharing
        fields = [
            'id',
            'dealtype',
            'dealstate',
            'sharing_feed_title',
            'img_url',
            # 작성자 이름,
            'pub_date',
            'view_cnt'
            # 좋아요,
            # 책갈피,
            # 댓글
        ]

class ExchangeSharingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeSharingImage
        fields = ['exchangesharing', 'image']
