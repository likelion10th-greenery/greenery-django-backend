from django.urls import path
from django.urls import path, include

from accounts import views
from accounts import kakao_auth
from accounts import naver_auth


app_name = 'accounts'

urlpatterns = [
    path('login/kakao/', kakao_auth.kakao_login),
    path('login/kakao/callback/', kakao_auth.kakao_callback),
    path('signup/',views.signup),
    path('login/',views.login),
    path('logout/',views.logout),
    path('update/<int:pk>/',views.user_update),
    path('delete/<int:pk>/',views.user_delete),
]