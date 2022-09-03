from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from accounts import views
from accounts import kakao_auth


app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup2, name="signup"),

    path('login/kakao/', kakao_auth.kakao_login),
    path('login/kakao/callback/', kakao_auth.kakao_callback),
]