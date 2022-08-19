from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    user_address = models.CharField(max_length=200, blank = True, null = True),
    user_bool = models.BooleanField(default=False)