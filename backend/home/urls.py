from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', get_all_tags),
]