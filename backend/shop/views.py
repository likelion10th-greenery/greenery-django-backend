from django.db import transaction
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
from home.serializers import TagSerializer

# Create your views here.

class PlantImageViewSet(ModelViewSet):
    """
    상점 판매글의 이미지 클래스뷰
    """
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer
    
    def perform_create(self, serializer):
        serializer.save()

        image = PlantImage.objects.last()
        if image.plant.img_url == 'default_img':
            image.plant.img_url = image.image
        else:
            image.plant.img_cnt += 1
        image.plant.save()


@api_view(['GET'])
def get_all_plants(request):
    '''
    모든 식물 조회 (shop main)
    '''
    reqcategory = request.GET.get('category', None)
    query = request.GET.get('query', None)
    order = request.GET.get('filter', None)
    q = Q()
    if reqcategory:
        q &= Q(category = reqcategory)  # 쿼리스트링으로 카테고리 필터링 (ex. shop/?category=flower)
    if query:
        q &= Q(plant_name__contains=query) # 쿼리스트링으로 원하는 식물 찾기 (ex. shop/?query=장미)
    # 카테고리와 원하는 식물 둘 다 적용하고 싶다면? ▶ (ex. shop/?cateogry=flower&query=장미)

    # ▼ 정렬 (기본은 최신순)   
    plants = Plant.objects.filter(q).order_by('-pub_date')
    if order == 'popular':
        plants = plants.order_by('-view_cnt')
    elif order == 'low':
        plants = plants.order_by('price')
    elif order == 'high':
        plants = plants.order_by('-price')

    plant_serializer = PlantSerializer(plants, many=True)
    return Response(plant_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@transaction.atomic()
def get_one_plant(request, id):
    '''
    id 값을 통한 식물 디테일 페이지 조회
    '''
    try:
        images = PlantImage.objects.filter(plant = id)
        imgserializer = PlantImageSerializer(images, many=True)
        plant = Plant.objects.get(id=id)
        serializer = PlantDetailSerializer(plant)
        plant.add_view_cnt()
        res = {
            "data" : serializer.data,
            "image" : imgserializer.data
        }
        plant.save()
        return Response(res, status=status.HTTP_200_OK)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


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
def shop_post(request):
    '''
    상점 판매글 등록
    '''
    try:
        serializer = PlantRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        plant = Plant.objects.last()
        if plant.shop_tags:
            for tag in plant.shop_tags.split(): # 태그 관련
                duplicated_tag = find_duplicate_tags(tag)
                if not duplicated_tag:
                    tag_serializer = TagSerializer(data=request.data)
                    if tag_serializer.is_valid(raise_exception=True):
                        tag_serializer.save(tag = tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def shop_update(request,pk):
    """
    상점 판매글 수정
    """
    try:
        post = Plant.objects.get(pk=pk)
        serializer = PlantRegisterSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()

            for tag in post.shop_tags.split(): # 태그 관련
                duplicated_tag = find_duplicate_tags(tag)
                if not duplicated_tag:
                    tag_serializer = TagSerializer(data=request.data)
                    if tag_serializer.is_valid(raise_exception=True):
                        tag_serializer.save(tag = tag)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def shop_delete(request, pk):
    """
    상점 판매글 삭제
    """
    try:
        post = Plant.objects.get(pk=pk)
        post.delete()
        return Response("삭제되었습니다!", status=status.HTTP_204_NO_CONTENT)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)