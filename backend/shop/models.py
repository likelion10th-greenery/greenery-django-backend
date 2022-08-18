from django.db import models

CATEGORIES = (
        ('FLOWER', '꽃'),
        ('FOLIAGE', '관엽/공기정화'),
        ('SUCCULENCE', '다육식물'),
        ('WILD', '야생화/분재'),
        ('ORCHID', '동/서양란'),
        ('SEED', '묘묙/씨앗'),
        ('ELSE', '기타'),
    )

ORIGIN = (
    ('DOMESTIC', '국내산'),
    ('IMPORT', '수입산'),
    ('ELSE', '모름'),
)

DELIVERY = (
    ('COURIER', '택배'),
    ('DIRECT', '직거래'),
    ('BOTH', '상관 없음'),
)

class Plant(models.Model):
    # ------------------ shop main -------------------- #
    feed_title= models.CharField(max_length=50, default="꽃 구경하세요:)") #게시글의 제목
    plant_type = models.CharField(max_length=50) # 식물명 데이터 베이스 만들었어요~
    price = models.IntegerField()
    # ------------------ register -------------------- #
    category = models.CharField(max_length=50, choices=CATEGORIES)
    stock = models.IntegerField(default=0) # pdf에는 등록할 때 재고 입력하는 칸 없음
    origin = models.CharField(max_length=50, choices=ORIGIN) # enum 아는 사람 손
    plant_width = models.FloatField(blank=True, null=True)
    plant_vertical = models.FloatField(blank=True, null=True)
    plant_height = models.FloatField(blank=True, null=True)
    pot_type = models.CharField(max_length=100, blank=True, null=True)
    deliver_type = models.CharField(max_length=50, choices=DELIVERY) # enum 아는 사람 손
    plant_detail = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=1000) #지역 3개까지 ","로 연결해서 저장
    view_cnt= models.IntegerField(default=0) # 조회수
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) # 마찬가지로 날짜는 pdf는 없는 요소

    def __str__(self):
        return self.plant_type

    def add_view_cnt(self):
        self.view_cnt+=1

class Tag(models.Model):
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    tag = models.TextField()

    def __str__(self):
        return self.tag
        
class PlantImage(models.Model):
    """
    이미지 필요할 때, view에서 찾아서 뿌려주는걸료..?
    대표 이미지는 image_number 값이 1인 값입니다.
    """
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image_url = models.TextField()
    image_number = models.IntegerField()  
    # 근데 img_number가 한 아이디당 10까지만 되는 게 아니라 연속 숫자로 계속 불어나는 게 아닌가? 
    # -> 이건 프론트 단에서 입력하는 칸 갯수를 막으면 돼요!

class PlantType(models.Model):
    type=models.CharField(max_length=100)