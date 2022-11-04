from django.urls import path

from accounts import views
from accounts import kakao_auth


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

# query parameter로 받아서 login 합치기