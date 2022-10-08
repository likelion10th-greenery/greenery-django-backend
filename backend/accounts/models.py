from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=11)
    user_address = models.CharField(max_length=200, blank = True, null = True)
    user_bool = models.BooleanField(default=False)

