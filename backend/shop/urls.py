from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'shop'

router = DefaultRouter()
router.register('shopimage', PlantImageViewSet, basename='shopimage')

urlpatterns = [
    path('', get_all_plants),
    path('<int:id>/', get_one_plant),
    path('register/', shop_post),
    path('<int:pk>/update', shop_update),
    path('<int:pk>/delete', shop_delete),

    # 이미지를 추가할 수 있는 링크
    path('img/', include(router.urls)), 
]
