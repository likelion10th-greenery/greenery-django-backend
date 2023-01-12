from .models import *
from .serializers import *
from django.db import transaction
from django.db.models import Q
from home.serializers import TagSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

class ExchangeSharingImageViewSet(ModelViewSet):
    """
    교환/나눔 작성글의 이미지 클래스뷰
    """
    queryset = ExchangeSharingImage.objects.all()
    serializer_class = ExchangeSharingImageSerializer
    
    def perform_create(self, serializer):
        serializer.save()

        image = ExchangeSharingImage.objects.last()
        if image.exchangesharing.img_url == 'default_url':
            image.exchangesharing.img_url = image.image
        else:
            image.exchangesharing.img_cnt += 1
        image.exchangesharing.save()

@api_view(['GET'])
def get_all(request):
    '''
    교환/나눔 식물 조회 (share main)
    '''
    reqtype = request.GET.get('dealtype', None)
    reqstate = request.GET.get('dealstate', None)
    reqitem = request.GET.get('dealitem', None)
    q = Q()
    if reqtype:
        q &= Q(dealtype = reqtype)
    if reqstate:
        q &= Q(dealstate = reqstate)
    if reqitem:
        q &= Q(dealitem = reqitem) # 쿼리스트링으로 필터 적용 가능 (ex. sharing/?dealtype=exchange&dealitem=seed)
    
    
    plants = ExchangeSharing.objects.filter(q)
    serializers = GetAll(plants, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.atomic()
def get_one(request, id):
    '''
    id값을 통한 교환/나눔 작성글 보기
    '''
    try:
        images = ExchangeSharingImage.objects.filter(exchangesharing = id)
        imgserializer = ExchangeSharingImageSerializer(images, many=True)
        post = ExchangeSharing.objects.get(id=id)
        post.add_view_cnt()
        if post.dealtype == "exchange":
            serializer = ExchangeSerializer(post)
        else:
            serializer = SharingSerializer(post)
        res = {
            "data" : serializer.data,
            "image" : imgserializer.data
        }

        return Response(res, status=status.HTTP_200_OK)
    except ExchangeSharing.DoesNotExist:
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
def sharing_post(request):
    """
    교환/나눔 글 작성
    """
    if request.user.is_authenticated: # 사용자 인증

        if request.data['dealtype'] == "exchange": # 거래타입이 '교환'일 경우
            serializer = ExchangeSerializer(data = request.data)
        else: # 거래타입이 '나눔'일 경우
            serializer = SharingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            post = ExchangeSharing.objects.last()
            if post.sharing_tags:
                for tag in post.sharing_tags.split(): # 태그 관련
                    duplicated_tag = find_duplicate_tags(tag)
                    if not duplicated_tag:
                        tag_serializer = TagSerializer(data=request.data)
                        if tag_serializer.is_valid(raise_exception=True):
                            tag_serializer.save(tag = tag)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    else: # 사용자 인증이 안 되었을 때
        return Response("로그인이나 회원 가입 후 이용해주세요.", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
def sharing_update(request,pk):
    """
    교환/나눔 글 수정
    """
    try:
        post = ExchangeSharing.objects.get(pk=pk)
        if post.dealtype == 'exchange':
            serializer = ExchangeSerializer(post, data=request.data)
        else:
            serializer = SharingSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()

            for tag in post.sharing_tags.split(): # 태그 관련
                duplicated_tag = find_duplicate_tags(tag)
                if not duplicated_tag:
                    tag_serializer = TagSerializer(data=request.data)
                    if tag_serializer.is_valid(raise_exception=True):
                        tag_serializer.save(tag = tag)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except ExchangeSharing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def sharing_delete(request, pk):
    """
    교환/나눔 글 삭제
    """
    try:
        post = ExchangeSharing.objects.get(pk=pk)
        post.delete()
        return Response("삭제되었습니다!", status=status.HTTP_204_NO_CONTENT)
    except ExchangeSharing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)