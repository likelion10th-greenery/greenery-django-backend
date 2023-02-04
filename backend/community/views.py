from .models import *
from .serializers import *
from home.serializers import TagSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from django.db import transaction

from accounts.models import PlantProfile

def find_duplicate_tags(tag):
    """
    중복태그 검출로직
    """
    try:
        return Tag.objects.get(tag = tag)
    except:
        return False


"""
식물일지 - Plant Diary
"""

class DiaryImageViewSet(ModelViewSet):
    """
    커뮤니티 - 식물일지의 이미지 클래스뷰
    """
    queryset = DiaryImage.objects.all()
    serializer_class = DiaryImageSerializer
    
    def perform_create(self, serializer):
        serializer.save()

        image = DiaryImage.objects.last()
        print(image.diary.img_url)
        if image.diary.img_url == "default_img":
            image.diary.img_url = image.image
        image.diary.save()



@api_view(['GET'])
def get_all_diaries(request):
    '''
    모든 식물 일지 조회 (community main)
    '''
    diary = PlantDiary.objects.all()
    serializer = DiaryMainSerializer(diary, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.atomic()
def get_one_plantdiary(request, id):
    """
    한 식물일지 조회 (plantdiary detail)
    """
    try:
        images = DiaryImage.objects.filter(diary = id)
        imgserializer = DiaryImageSerializer(images, many=True)
        diary = PlantDiary.objects.get(id=id)
        serializer = DiaryDetailSerializer(diary)
        res = {
            "data" : serializer.data,
            "image" : imgserializer.data
        }
        diary.save()
        return Response(res, status=status.HTTP_200_OK)
    except diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def plantdiary_register(request):
    """
    식물일지 등록하기
    """
    if request.user.is_authenticated: # 사용자 인증
        serializer = DiaryPostSerializer(data = request.data)
        if serializer.is_valid():
            try:
                plant = PlantProfile.objects.get(nickname = serializer.validated_data['plantprofile'])
                serializer.validated_data['category'] = plant.category
                serializer.validated_data['place'] = plant.place
                serializer.validated_data['year'] = str(plant.start_day)[:4]
                serializer.validated_data['month'] = str(plant.start_day)[5:7]
                serializer.validated_data['day'] = str(plant.start_day)[8:10]
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PlantProfile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("로그인이나 회원가입 후 이용해주세요", status=status.HTTP_401_UNAUTHORIZED)


"""
질의응답 - QnA
"""

class QnaImageViewSet(ModelViewSet):
    """
    커뮤니티 - 질의응답의 이미지 클래스뷰
    """
    queryset = QnAImage.objects.all()
    serializer_class = QnAImageSerializer
    
    def perform_create(self, serializer):
        serializer.save()

        image = QnAImage.objects.last()
        if not image.qna.img_url:
            image.qna.img_url = image.image
        else:
            image.qna.img_cnt += 1
        image.qna.save()


@api_view(['GET'])
def get_all_qna(request):
    '''
    커뮤니티 - 질의응답 질문글 조회 (community-QnA main)
    '''
    posts = QnA.objects.all()
    serializers = QnAMainSerializer(posts, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.atomic()
def get_one_qna(request, id):
    '''
    커뮤니티 - 질의응답 질문글의 디테일 페이지 (id값으로)
    '''
    try:
        images = QnAImage.objects.filter(qna = id)
        imgserializer = QnAImageSerializer(images, many=True)
        post = QnA.objects.get(id=id)
        post.add_view_cnt()
        serializer = QnADetailSerializer(post)
        res = {
            "data" : serializer.data,
            "image" : imgserializer.data
        }
        return Response(res, status=status.HTTP_200_OK)
    except QnA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def qna_post(request):
    """
    커뮤니티 - 질의응답 질문글 등록
    """
    if request.user.is_authenticated:
        serializer = QnAPostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            post = QnA.objects.last()
            if post.qna_tags:
                for tag in post.qna_tags.split(): # 태그 관련
                    duplicated_tag = find_duplicate_tags(tag)
                    if not duplicated_tag:
                        tag_serializer = TagSerializer(data=request.data)
                        if tag_serializer.is_valid(raise_exception=True):
                            tag_serializer.save(tag = tag)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("로그인이나 회원 가입 후 이용 해주세요", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
def qna_update(request,pk):
    """
    커뮤니티 - 질의응답 질문글 수정
    """
    try:
        post = QnA.objects.get(pk=pk)
        serializer = QnAPostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()

            for tag in post.qna_tags.split(): # 태그 관련
                duplicated_tag = find_duplicate_tags(tag)
                if not duplicated_tag:
                    tag_serializer = TagSerializer(data=request.data)
                    if tag_serializer.is_valid(raise_exception=True):
                        tag_serializer.save(tag = tag)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except QnA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def qna_delete(request, pk):
    """
    커뮤니티 - 질의응답 질문글 삭제
    """
    try:
        post = QnA.objects.get(pk=pk)
        post.delete()
        return Response("삭제되었습니다!", status=status.HTTP_204_NO_CONTENT)
    except QnA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)