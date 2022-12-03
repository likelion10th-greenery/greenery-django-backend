from django.urls import path
from accounts import views
from accounts import kakao_auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.TokenSignupAPIView.as_view()),
    path('login/', views.TokenLoginAPIView.as_view()),
    path('logout/',views.logout),
    path('update/<int:pk>/',views.user_update),
    path('delete/<int:pk>/',views.user_delete),
    path('getuser', views.get_all_user),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify')
]

kakaologin = [
    path('login/kakao/', kakao_auth.kakao_login),
    path('login/kakao/callback/', kakao_auth.kakao_callback),
]

urlpatterns += kakaologin