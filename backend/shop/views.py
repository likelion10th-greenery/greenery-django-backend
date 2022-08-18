from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Plant
from .serializers import PlantSerializer, PlantRegisterSerializer, PlantImageRegisterSerializer, TagSerializer

# Create your views here.

'''
모든 식물 조회
'''
@api_view(['GET'])
def get_all_plants(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

'''
카테고리별로 식물 조회
''' 
@api_view(['GET'])
def get_classified_plants(request, type):
    plants = Plant.objects.filter(category=type)
    try:
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

'''
한 식물 디테일 페이지 조회 (id값으로)
'''
@api_view(['GET'])
def get_one_plant(request, id):
    plant = Plant.objects.get(id=id)
    try:
        serializer = PlantRegisterSerializer(plant)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

'''
키워드로 식물 찾기
'''
@api_view(['GET'])
def search(request):
    query = request.GET.get('query', None)
    if query:
        try:
            plants = Plant.objects.filter(plant_name__contains=query)
            serializer = PlantSerializer(plants, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

'''
식물 등록
'''
@api_view(['POST'])
def register_plant(request):
    try:
        with transaction.atomic():
            plant_serializer = PlantRegisterSerializer(data=request.data)  
            if plant_serializer.is_valid():
                plant_serializer.save()

            plant_images = request.data.get("plant_images")
            for plant_image in plant_images:
                image_serializer=PlantImageRegisterSerializer(data=plant_image)
                if image_serializer.is_valid():
                    image_serializer.save()
                    
            plant_serializer.data["plant_images"]=str(request.data.get("plant_images"))
            return Response(plant_serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

'''
태그 등록
'''
@api_view(['POST'])
def create_tag(request, id):
    plant = Plant.objects.get(id=id)
    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(plant_id=plant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
