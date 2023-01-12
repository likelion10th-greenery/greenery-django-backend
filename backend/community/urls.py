from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'community'

router = DefaultRouter()
router.register('sharingimage', ExchangeSharingImageViewSet, basename='sharingimage')

urlpatterns = [
    path('', plant_diary),
    
    path('qna/', get_all_qna),
    path('qna/<int:id>', get_one_qna),
    path('qna/post', qna_post),
    path('qna/<int:pk>/update', qna_update),
    path('qna/<int:pk>/delete', qna_delete),
    # 이미지를 추가할 수 있는 링크
    path('qna/img/', include(router.urls)), 
]