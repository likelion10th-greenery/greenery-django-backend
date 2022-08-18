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
    plant_name = models.CharField(max_length=50) # 나중에 식물명 데이터 베이스에서 고르는 형식으로 바꾸겠음.
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
        return self.plant_name

class PlantImage(models.Model):
    """
    이미지 필요할 때, view에서 찾아서 뿌려주는걸료..?
    """
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image_url = models.TextField()
    image_number = models.IntegerField()  
    is_rep = models.BooleanField(blank=True)
    # 근데 이 필드가 무한으로 생성되는 거 아님? (그렇게 해달라고 하셨다 맞다)
    # 근데 img_number가 한 아이디당 10까지만 되는 게 아니라 연속 숫자로 계속 불어나는 게 아닌가?
    # 함수를 만들 수 있으려나? 일단 해보고 함수를 만들자
    # 함수 : 같은 plant_id를 가진 필드라면 나중에 올린 image_number이 후에 올린 image_number보다 하나 크도록.
    # 그럼 자동생성이랑 다를 게 뭐야 / 일단 자동생성으로 해보자.