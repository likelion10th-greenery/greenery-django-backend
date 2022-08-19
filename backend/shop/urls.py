from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', get_all_plants),
    path('<int:id>/', get_one_plant),
    path('register/', register_plant),
    path('search', search), # search?query=[식물이름]
    path('tag/<int:id>', create_tag),
    path('crawler', update_plant_type),
    path('<str:type>/', get_classified_plants),
]
# <str:type>이 들어 있으면 맨 밑으로 내려야 한다