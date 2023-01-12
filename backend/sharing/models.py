from django.db import models
from home.models import Tag

# ▼ AI, 와이어프레임은 아래에서 참고.
# https://www.notion.so/likelion-hufs-greenery/2-Share-4987c1eaaa764d03aebb51392a05df6d

# 거래방법
DEALTYPE = (
    ('exchange', '교환'),
    ('sharing', '나눔')
)

# 거래상태
DEALSTATE = (
    ('yet', '거래 전'),
    ('progress', '거래 중'),
    ('finished', '거래 완료')
)

# 거래품목
DEALITEM = (
    ('seed', '씨앗'),
    ('seedling', '모종/삽수'),
    ('goods', '원예용품')
)

# 교환/나눔 모델
class ExchangeSharing(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    dealtype = models.CharField(max_length=50, choices=DEALTYPE)
    dealstate = models.CharField(max_length=50, choices=DEALSTATE)
    dealitem = models.CharField(max_length=50, choices=DEALITEM)
    sharing_feed_title = models.CharField(max_length=200)
    item = models.CharField(max_length=50, default="식물")
    view_cnt= models.IntegerField(default=0) # 조회수
    # 대표 이미지, 이미지가 없으면 디폴트값을 가지고 있으면 가장 첫 번째 값을 가진다.
    img_url = models.TextField(default="default_url")
    img_cnt = models.IntegerField(default=0)
    #  교환 항목
    exchange_method = models.TextField(default="직거래, 택배 등")
    communicate_method = models.TextField(default="카카오톡 아이디, 이메일, 연락처 등")
    # 나눔 항목
    sharing_method = models.TextField(default="우편, 택배착불, 직거래 등")
    selection_method = models.TextField(default="댓글 선착순, 랜덤 추첨 등")
    notice_date = models.TextField(default="미정")
    # 자율 추가 항목
    add_text = models.TextField(blank=True, null=True)
    # 태그
    tagDB = models.ManyToManyField(Tag, related_name='sharing_tags')
    sharing_tags = models.TextField(blank=True, null=True)

    def __str__(self):
        return "[" + self.dealtype + "] " + self.item

    def add_view_cnt(self):
        self.view_cnt += 1

class ExchangeSharingImage(models.Model):
    exchangesharing = models.ForeignKey(ExchangeSharing, on_delete=models.CASCADE)
    image = models.TextField()

    def __str__(self):
        return self.image