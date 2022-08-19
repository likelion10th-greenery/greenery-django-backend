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
    tag = models.TextField()

    def __str__(self):
        return self.tag


class Plant(models.Model):
    """
    식물 피드 모델
    """
    # ------------------ shop main -------------------- #
    feed_title= models.CharField(max_length=50, default="꽃 구경하세요:)") #게시글의 제목
    plant_type = models.CharField(max_length=50) # 식물명 데이터 베이스 만들었어요~
    price = models.IntegerField()
    view_cnt= models.IntegerField(default=0) # 조회수
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) # 마찬가지로 날짜는 pdf는 없는 요소
    tags= models.ManyToManyField(Tag, blank=True) #해시태그 들
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
    
    def __str__(self):
        return self.plant_type

    def add_view_cnt(self):
        self.view_cnt+=1

    def add_tag(self, tag):
        self.tags.add(tag)
        
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
    """
    식물 종류 모델
    """
    type=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.type