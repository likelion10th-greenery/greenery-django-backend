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
    nickname = models.CharField(max_length=50, unique=True)
    introduction = models.CharField(max_length=100,blank=True,null=True)
    instagram_id = models.TextField(max_length=50,blank=True,null=True)
    youtube_id = models.TextField(max_length=50,blank=True,null=True)
    blog_id = models.TextField(max_length=50,blank=True,null=True)
    profile_img = models.TextField(max_length=100,default='greenary')
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers',blank=True,null=True)