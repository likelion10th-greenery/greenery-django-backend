from django.db import models
from home.models import Tag

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

# 원산지
ORIGIN = (
    ('domestic', '국내산'),
    ('import', '수입산'),
    ('else', '모름'),
)

# 배달방법
DELIVERY = (
    ('courier', '택배'),
    ('direct', '직거래'),
    ('both', '상관 없음'),
)

class Plant(models.Model):
    """
    식물 피드 모델
    """
    feed_title= models.CharField(max_length=50, default = "꽃 구경하세요:)")
    plant_name = models.CharField(max_length=50, default = "식물") # 식물명 DB 안 써서 사용자 자율 입력
    category = models.CharField(max_length=50, choices=CATEGORIES)
    price = models.IntegerField() # 판매가
    stock = models.IntegerField(default=1)
    # ▼ 태그
    tagDB = models.ManyToManyField(Tag, related_name='shop_tags')
    shop_tags = models.TextField(blank=True, null=True)
    # ▼ 상품 주요 정보
    origin = models.CharField(max_length=50, choices=ORIGIN)
    plant_width = models.FloatField(blank=True, null=True) # 가로
    plant_vertical = models.FloatField(blank=True, null=True) # 세로
    plant_height = models.FloatField(blank=True, null=True) # 높이
    pot_type = models.CharField(max_length=100, blank=True, null=True) # 화분 종류
    deliver_type = models.CharField(max_length=50, choices=DELIVERY) # 배송 방법
    address = models.CharField(max_length=1000)
    # ▼ 상세 설명
    plant_detail = models.TextField(blank=True, null=True)
    # ▼ 기타
    view_cnt= models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    img_url = models.TextField(blank=True, null=True, default="default_img") # 메인 화면에 보일 대표 이미지
    img_cnt = models.IntegerField(default=0)
    
    def __str__(self):
        return self.plant_name

    def add_view_cnt(self):
        self.view_cnt += 1
        
class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image = models.TextField()

    def __str__(self):
        return self.image