from .models import CustomUser
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import LoginSerializer, SignupSerializer

# Create your views here.
"""
토큰회원가입
"""
class TokenSignupAPIView(APIView):
    def post(self, request):
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

"""
토큰 로그인
"""
class TokenLoginAPIView(APIView):
    def post(self, request):
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

'''
로그아웃
'''
@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return Response(status=status.HTTP_200_OK)

"""
유저 수정
"""
@api_view(['PUT'])
def user_update(request,pk):
    try:
        user = CustomUser.objects.get(pk=pk)
        serializer = SignupSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

"""
유저 삭제
"""
@api_view(['DELETE'])
def user_delete(request,pk):
    try:
        user = CustomUser.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# view LAB
"""
CustomUser list로 보기
"""
@api_view(["GET"])
def get_all_user(request):
    user = CustomUser.objects.all()
    serializer = LoginSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)