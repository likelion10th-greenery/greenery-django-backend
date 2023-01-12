from .models import *
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django.db import transaction


"""
유저 관련
"""

class TokenLoginAPIView(APIView):
    def post(self, request):
        """
        토큰 로그인
        """
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(username=serializer.data["username"])
            # if not check_password(request.data['password'], user.password):
            #     return Response({"msg" : "비밀번호가 틀렸습니다"}, status=status.HTTP_400_BAD_REQUEST)
        if user is not None:
            auth.login(request, user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user" : serializer.data['username'],
                    "message" : "로그인 성공!",
                    "token" : {
                        "access" : access_token,
                        "refresh" : refresh_token,
                    },
                },
                status=status.HTTP_200_OK
            )
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def logout(request):
    '''
    로그아웃
    '''
    auth.logout(request)
    return Response(status=status.HTTP_200_OK)
    

class TokenSignupAPIView(APIView):
    def post(self, request):
        """
        토큰회원가입
        """
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save(password = make_password(serializer.validated_data['password']))
            token = TokenObtainPairSerializer.get_token(new_user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user" : serializer.data['username'],
                    "message" : "회원가입 완료!",
                    "token" : {
                        "access" : access_token,
                        "refresh" : refresh_token,
                    }
                },
                status = status.HTTP_200_OK
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            auth.login(request, new_user)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def user_update(request,pk):
    """
    유저 수정
    """
    try:
        user = CustomUser.objects.get(pk=pk)
        serializer = SignupSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def user_delete(request,pk):
    """
    유저 삭제
    """
    try:
        user = CustomUser.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def get_all_user(request):
    """
    CustomUser list로 보기
    """
    user = CustomUser.objects.all()
    serializer = LoginSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


"""
식물 프로필 관련
"""

@api_view(['GET'])
def get_all_plantprofile(request):
    '''
    모든 식물프로필 조회 (plantprofile main)
    '''
    if request.user.is_authenticated: # 사용자 인증
        plants = PlantProfile.objects.all()
        serializer = PlantProfileSerializer(plants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("로그인이나 회원가입 후 이용해주세요", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@transaction.atomic()
def get_one_plantprofile(request, id):
    """
    한 식물프로필 조회 (plantprofile detail)
    """
    if request.user.is_authenticated: # 사용자 인증
        try:
            plant = PlantProfile.objects.get(id=id)
            serializer = PlantProfileDetailSerializer(plant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PlantProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response("로그인이나 회원가입 후 이용해주세요", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def plantprofile_register(request):
    """
    식물 프로필 등록하기
    """
    if request.user.is_authenticated: # 사용자 인증
        serializer = PlantProfileRegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("로그인이나 회원가입 후 이용해주세요", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
def profile_update(request,pk):
    """
    식물 프로필 수정
    """
    try:
        profile = PlantProfile.objects.get(pk=pk)
        serializer = PlantProfileRegisterSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except PlantProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def profile_delete(request, pk):
    """
    교환/나눔 글 삭제
    """
    try:
        post = PlantProfile.objects.get(pk=pk)
        post.delete()
        return Response("삭제되었습니다!", status=status.HTTP_204_NO_CONTENT)
    except PlantProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
