from django.http import JsonResponse
from django.db import transaction
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Plant, PlantImage, Tag
from .serializers import PlantSerializer, PlantRegisterSerializer, PlantImageRegisterSerializer, TagSerializer
from .utils.PlantTypeCrawler import PlantTypeCrawler

# Create your views here.

@api_view(['GET'])
def get_all_plants(request):
    '''
    모든 식물 조회
    '''
    plants = Plant.objects.all()
    data=list()
    for plant in plants:
        q=Q()
        q.add(Q(plant=plant), q.AND)
        q.add(Q(image_number=1), q.AND)
        images= PlantImage.objects.filter(q)    
        data.append([PlantRegisterSerializer(plant),PlantImageRegisterSerializer(images)])
    return Response(data)

# @api_view(["GET"])
# def get_all_plants(request):
#     '''
#     모든 식물 조회
#     '''
#     plants = Plant.objects.all()
#     serializer = PlantSerializer(many=True)
#     serializer.validated_data["img_url"] = 

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
                
                plant_tags= request.data.get("plant_tags")
                print(plant_tags)
                
                # for plant_tag in plant_tags:
                #     candidate_tag=plant_tag.get("tag").replace(" ","")
                #     duplicated_tag=find_duplicate_tags(candidate_tag)
                #     if not duplicated_tag:
                #         tag_serializer= TagSerializer(data=plant_tag)
                #         if tag_serializer.is_valid(raise_exception=True):
                #             tag=tag_serializer.save(tag=candidate_tag)
                #             plant.add_tag(tag)
                #             plant.save()
                #     else:
                #         plant.add_tag(duplicated_tag)
                #         plant.save()

                return Response(plant_serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def find_duplicate_tags(tag):
    """
    중복태그 검출로직
    """
    try:
        return Tag.objects.get(tag=tag)
    except:
        return False


def update_plant_type(request):
    PlantTypeCrawler().crawler()
    
    data = {'result': "DB update success"}
    return JsonResponse(data, status=status.HTTP_200_OK)