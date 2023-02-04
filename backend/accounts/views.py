from .models import CustomUser

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import *
from django.contrib.auth.hashers import make_password

from django.shortcuts import get_object_or_404, redirect

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginSerializer, SignupSerializer


# Create your views here.

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        if len(serializer.validated_data['nickname']) >= 2 and len(serializer.validated_data['nickname']) <= 10:
            if len(serializer.validated_data['password']) >= 8 and any(i.isalpha() for i in serializer.validated_data['password']) and any(i.isdigit() for i in serializer.validated_data['password']):   
                if serializer.validated_data['password'] == serializer.validated_data['password1']:
                    new_user = serializer.save(password = make_password(serializer.validated_data['password']))
                    auth.login(request, new_user)
                    return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status=status.HTTP_400_BAD_REQUEST)

'''
로그인
'''
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = auth.authenticate(
            request = request, 
            username = serializer.data['username'],
            password = serializer.data['password']
        )
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            auth.login(request, user)
            return Response({'token':token.key}, status=status.HTTP_200_OK)
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

"""
팔로우, 팔로잉
"""
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')