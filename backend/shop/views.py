from django.http import JsonResponse
from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Plant
from .serializers import PlantSerializer, PlantRegisterSerializer, PlantImageRegisterSerializer, TagSerializer
from .utils.PlantTypeCrawler import PlantTypeCrawler

# Create your views here.

@api_view(['GET'])
def get_all_plants(request):
    '''
    모든 식물 조회
    '''
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_classified_plants(request, type):
    '''
    카테고리별로 식물 조회
    ''' 
    plants = Plant.objects.filter(category=type)
    try:
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_one_plant(request, id):
    '''
    한 식물 디테일 페이지 조회 (id값으로)
    '''
    try:
        with transaction.atomic():
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


@api_view(['POST'])
def register_plant(request):
    '''
    식물 등록
    '''
    try:
        with transaction.atomic():
            plant_serializer = PlantRegisterSerializer(data=request.data)  
            if plant_serializer.is_valid(raise_exception=True):
                plant_serializer.save()

                plant_images = sorted(request.data.get("plant_images"),key=lambda x: x["image_number"])
                plant = Plant.objects.last()
                for idx, plant_image in enumerate(plant_images, start=1):
                    image_serializer=PlantImageRegisterSerializer(data=plant_image, partial=True)
                    if image_serializer.is_valid(raise_exception=True):
                        image_serializer.save(plant=plant, image_number=idx)
                return Response(plant_serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_tag(request, id):
    '''
    태그 등록
    '''
    plant = Plant.objects.get(id=id)
    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(plant_id=plant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def update_plant_type(request):
    PlantTypeCrawler().crawler()
    
    data = {'result': "DB update success"}
    return JsonResponse(data, status=status.HTTP_200_OK)