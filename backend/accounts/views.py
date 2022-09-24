from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer
from django.contrib import auth
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        if len(serializer.validated_data['password']) >= 8 and any(i.isalpha() for i in serializer.validated_data['password']) and any(i.isdigit() for i in serializer.validated_data['password']):   
            if serializer.validated_data['password'] == serializer.validated_data['password1']:
                new_user = serializer.save(password = make_password(serializer.validated_data['password']))
                auth.login(request, new_user)
                return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

'''
로그인
'''
@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = auth.authenticate(
            request = request, 
            username = serializer.data['username'],
            password = serializer.data['password']
        )
        if user is not None:
            auth.login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
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