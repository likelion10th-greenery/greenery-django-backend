from django.db import models
from accounts.models import CustomUser
from home.models import Tag

# Create your models here.

"""
커뮤니티 - 식물일지
"""

ORDERS = (
        ('latest', '최신순'),
        ('count', '조회순'),
        ('like', '좋아요순'),
        ('comment', '댓글순'),
    )

CATEGORIES = (
        ('flower', '꽃'),
        ('foliage', '관엽/공기정화'),
        ('succulence', '다육식물'),
        ('wild', '야생화/분재'),
        ('orchid', '동/서양란'),
        ('seed', '묘묙/씨앗'),
        ('else', '기타'),
    )

PLACES = (
        ('indoor', '실내'),
        ('outdoor', '야외'),
    )

class PlantDiary(models.Model):
    plantprofile = models.CharField(max_length=50, default="미정")
    title = models.CharField(max_length=100, default="제목 없음")
    category = models.CharField(blank=True, null=True, max_length=50, choices=CATEGORIES)
    place = models.CharField(blank=True, null=True, max_length=50, choices=PLACES)
    sun = models.IntegerField(default=3)
    water = models.IntegerField(default=3)
    year = models.IntegerField(default=2020)
    month = models.IntegerField(default=1)
    day = models.IntegerField(default=1)
    view_cnt = models.IntegerField(default=0)
    plant_tags = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True, default='default_img')
    body = models.TextField(blank=True, null=True, default="")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DiaryImage(models.Model):
    diary = models.ForeignKey(PlantDiary, on_delete=models.CASCADE)
    image = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.image


"""
커뮤니티 - 질의응답
"""
class QnA(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, default='질문')
    body = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    img_cnt = models.IntegerField(default=0)
    qna_tags = models.TextField(blank=True, null=True)
    view_cnt= models.IntegerField(default=0) # 조회수

    def __str__(self):
        return self.title

    def add_view_cnt(self):
        self.view_cnt += 1

class QnAImage(models.Model):
    qna = models.ForeignKey(QnA, on_delete=models.CASCADE)
    image = models.TextField()

    def __str__(self):
        return self.image