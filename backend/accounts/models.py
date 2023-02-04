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


# {
# "username" : "Sally",
# "password" : "sallybelly12!",
# "password1" : "sallybelly12!",
# "phone_num" : "01012341234"
# }

# 카테고리
CATEGORIES = (
        ('flower', '꽃'),
        ('foliage', '관엽/공기정화'),
        ('succulence', '다육식물'),
        ('wild', '야생화/분재'),
        ('orchid', '동/서양란'),
        ('seed', '묘묙/씨앗'),
        ('else', '기타'),
    )

# 키우는 장소
PLACES = (
    ('indoor', '실내'),
    ('outdoor', '야외')
)

class PlantProfile(models.Model):
    nickname = models.CharField(max_length=40)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    place = models.CharField(max_length=50, choices=PLACES)
    start_day = models.DateField()
    pub_date = models.DateTimeField(auto_now=True)
    img_url = models.TextField(blank=True, null=True, default="default_img")

    def __str__(self):
        return self.nickname

