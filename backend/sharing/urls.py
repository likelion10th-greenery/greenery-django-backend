from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'sharing'

router = DefaultRouter()
router.register('sharingimage', ExchangeSharingImageViewSet, basename='sharingimage')

urlpatterns = [
    path('', get_all),
    path('<int:id>', get_one),
    path('posting/', sharing_post),
    path('<int:pk>/update', sharing_update),
    path('<int:pk>/delete', sharing_delete),

    # 이미지를 추가할 수 있는 링크
    path('img/', include(router.urls)), 
]