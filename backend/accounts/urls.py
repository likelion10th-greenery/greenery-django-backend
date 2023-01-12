from django.urls import include, path
from accounts import views
from accounts import kakao_auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'accounts'

# 유저 관련
urlpatterns = [
    path('', views.TokenLoginAPIView.as_view()),
    path('logout/',views.logout),
    path('signup/', views.TokenSignupAPIView.as_view()),
    path('<int:pk>/update',views.user_update),
    path('<int:pk>/delete/',views.user_delete),
    path('getuser', views.get_all_user),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),

    path('login/kakao/', kakao_auth.kakao_login),
    path('login/kakao/callback/', kakao_auth.kakao_callback),
]

plantprofile = [
    path('plantprofile/', views.get_all_plantprofile),
    path('plantprofile/<int:id>/', views.get_one_plantprofile),
    path('plantprofile/register/', views.plantprofile_register),
    path('plantprofile/<int:pk>/update', views.profile_update),
    path('plantprofile/<int:pk>/delete', views.profile_delete),
]

urlpatterns += plantprofile