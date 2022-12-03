import requests

from django.shortcuts import redirect
from django.contrib.auth import login

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from  . import models as user_models

class KakaoException(Exception):
      pass

@api_view(['GET'])
def kakao_login(request):
    #이후 env 파일에 추가 필요
    rest_api_key= "6fec2af22db6826a94eba707eac15af5"
    #이후 도메인에 따른 수정 필요
    callback_url='http://127.0.0.1:8000/accounts/login/kakao/callback/'
    redirect_url= f"kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={callback_url}&response_type=code"

    print("ok1")
    return redirect(f"https://{redirect_url}")

@api_view(['GET'])
def kakao_callback(request):
    try:    
        print("ok2")
        rest_api_key= "6fec2af22db6826a94eba707eac15af5"
        callback_url='http://127.0.0.1:8000/accounts/login/kakao/callback/'
        code=request.GET.get("code")
        
        print(code)
            
        token_request= requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={callback_url}&code={code}"
        )
        token_response_json=token_request.json()
        error=token_response_json.get("error",None)
        print(f"token_response_json : {token_response_json}")

        if error is not None:
            raise KakaoException("can not import kakao authorization code.")

        access_token=token_response_json.get("access_token")
        profile_request=requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        profile_json=profile_request.json()

        print(f"Profile : {profile_json}")
        try:
            user=user_models.CustomUser.objects.get(username=profile_json.get("kakao_account").get("email"))
        except:
            user=user_models.CustomUser.objects.create(
                username=profile_json.get("kakao_account").get("email")
            )
            user.set_unusable_password()
            user.save()
        
        print("user",user.username)
        login(request,user)
        print("로그인 됐을걸요? 아마..?")

        return Response(status=status.HTTP_200_OK)

    except KakaoException as error:
        return Response(status=status.HTTP_400_BAD_REQUEST)