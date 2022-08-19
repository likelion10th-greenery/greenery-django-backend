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
        print("일단 valid")
        serializer.save(commit=False)
        if len(serializer.password1) >= 8 and len(str(serializer.user_num)) == 11:
            alpha_flag = False
            num_flag = False
            for i in serializer.password1:
                if i.isnum():
                    num_flag = True
                elif i.isalpha():
                    alpha_flag = True
                if num_flag and alpha_flag:
                    break
            if serializer.password1 == serializer.password2:
                new_user = serializer.save(password = make_password(serializer.validated_data['password1']))
        auth.login(request, new_user)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup2(request):
    print("!")
    serializer = SignupSerializer(data=request.data)
    print("!!")
    if serializer.is_valid():
        print("!!!")
        new_user = serializer.save(password = make_password(serializer.validated_data['password1']))
        print("!!!!")
        auth.login(request, new_user)
        return Response(status=status.HTTP_200_OK)
    print(serializer.errors)
    return Response(status=status.HTTP_400_BAD_REQUEST)
