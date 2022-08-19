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
        if len(serializer.password) >= 8 and any(i.isnum() for i in serializer.password) and any(i.isdigit() for i in serializer.password):
            if serializer.password == serializer.password1:
                if len(str(serializer.user_num)) == 11:
                    new_user = serializer.save(password = make_password(serializer.validated_data['password']))
                    auth.login(request, new_user)
                    return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup2(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        new_user = serializer.save(password = make_password(serializer.validated_data['password1']))
        auth.login(request, new_user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    print(serializer.errors)
    return Response(status=status.HTTP_400_BAD_REQUEST)
