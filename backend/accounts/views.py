from fcntl import F_GETLEASE
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer
from django.contrib import auth

# Create your views here.

def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(commit=False)
        if len(serializer.password1) >= 8:
            alpha_flag = False
            num_flag = False
            for i in serializer.password1:
                if i.isnum():
                    num_flag = True
                elif i.isalpha():
                    alpha_flag = True
                if num_flag and alpha_flag:
                    break
        
        new_user = serializer.save(password = make_password(serializer.validated_data['password']))
        auth.login(request, new_user)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
