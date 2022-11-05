from django.db import models

CATEGORIES = (
        ('flower', '꽃'),
        ('foliage', '관엽/공기정화'),
        ('succulence', '다육식물'),
        ('wild', '야생화/분재'),
        ('orchid', '동/서양란'),
        ('seed', '묘묙/씨앗'),
        ('else', '기타'),
    )

ORIGIN = (
    ('domestic', '국내산'),
    ('import', '수입산'),
    ('else', '모름'),
)

DELIVERY = (
    ('courier', '택배'),
    ('direct', '직거래'),
    ('both', '상관 없음'),
)

class Tag(models.Model):
    """
    해시태그 모델
    """
    tag = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.tag

class Plant(models.Model):
    """
    식물 피드 모델 (shop main, register, detail 관련)
    """
    # ------------------ shop main -------------------- #
    feed_title= models.CharField(max_length=50, default = "꽃 구경하세요:)")
    plant_type = models.CharField(max_length=50) # 추후 수정 예정 (식물명 데이터 베이스가 완성되었기 때문)
    price = models.IntegerField()
    view_cnt= models.IntegerField(default=0) # 조회수
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) # PM측 지정 요소는 아님
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags') # 해시태그
    plant_tags = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    # ------------------ register -------------------- #
    category = models.CharField(max_length=50, choices=CATEGORIES)
    stock = models.IntegerField(default=0) # PM측 지정 요소는 아님
    origin = models.CharField(max_length=50, choices=ORIGIN)
    plant_width = models.FloatField(blank=True, null=True) # 가로
    plant_vertical = models.FloatField(blank=True, null=True) # 세로
    plant_height = models.FloatField(blank=True, null=True) # 높이
    pot_type = models.CharField(max_length=100, blank=True, null=True) # 화분 종류
    deliver_type = models.CharField(max_length=50, choices=DELIVERY)
    plant_detail = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.plant_type

    def add_view_cnt(self):
        self.view_cnt += 1

    def add_tag(self, tag):
        self.tags.add(tag)
        
class PlantImage(models.Model):
    """
    식물 이미지 (대표사진은 image_number가 1)
    """
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image_url = models.TextField(blank=True, null=True)
    image_number = models.IntegerField()
    
    def __str__(self):
        return self.image_url

class PlantType(models.Model):
    """
    식물 종류 모델 (crawler 관련)
    """
    type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.type