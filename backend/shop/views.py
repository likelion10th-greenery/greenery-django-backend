from functools import partial
from django.http import JsonResponse
from django.db import transaction
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Plant, PlantImage, Tag
from .serializers import PlantSerializer, PlantRegisterSerializer, PlantImageSerializer, TagSerializer
from .utils.PlantTypeCrawler import PlantTypeCrawler

# Create your views here.

@api_view(['GET'])
def get_all_plants(request):
    '''
    모든 식물 조회 (shop main)
    '''
    plants = Plant.objects.all()
    plant_serializer = PlantSerializer(plants, many=True)
    return Response(plant_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_classified_plants(request, category):
    '''
    카테고리별 식물 조회
    ''' 
    print(category)
    plants = Plant.objects.filter(category__iexact=category)
    try:
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@transaction.atomic()
def get_one_plant(request, id):
    '''
    id 값을 통한 식물 디테일 페이지 조회
    '''
    try:
        plant = Plant.objects.get(id=id)
        plant.add_view_cnt()
        plant.save()
        serializer = PlantRegisterSerializer(plant)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def search(request):
    '''
    키워드로 식물 찾기
    '''
    query = request.GET.get('query', None)
    if query:
        try:
            plants = Plant.objects.filter(plant_type__contains=query)
            serializer = PlantSerializer(plants, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def find_duplicate_tags(tag):
    """
    중복태그 검출로직
    """
    try:
        return Tag.objects.get(tag = tag)
    except:
        return False


@api_view(['POST'])
@transaction.atomic()
def register_plant(request):
    '''
    식물 등록
    '''
    try:
        plant_serializer = PlantRegisterSerializer(data=request.data) # 식물 기본 정보 관련
        if plant_serializer.is_valid(raise_exception=True):
            plant_serializer.save()
        plant = Plant.objects.last()

        for tag in plant.plant_tags.split(): # 식물 태그 관련
            duplicated_tag = find_duplicate_tags(tag)
            if not duplicated_tag:
                tag_serializer = TagSerializer(data=request.data)
                if tag_serializer.is_valid(raise_exception=True):
                    tag_serializer.save(tag = tag)

        if request.data.get('plant_images'): # 식물 이미지 관련
            plant_images = sorted(request.data.get("plant_images"), key = lambda x: x["image_number"])
            for idx, img in enumerate(plant_images, start = 1):
                if idx == 1:
                    plant_serializer.save(img_url=img['image_url'])
                image_serializer = PlantImageSerializer(data=img, partial=True)
                if image_serializer.is_valid(raise_exception=True):
                    image_serializer.save(plant = plant, image_number = idx)
                    
        return Response(plant_serializer.data, status=status.HTTP_200_OK)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def update_plant_type(request):
    """
    크롤링을 통한 식물명 데이터베이스 생성
    """
    PlantTypeCrawler().crawler()
    data = {'result': "DB update success"}
    return JsonResponse(data, status=status.HTTP_200_OK)