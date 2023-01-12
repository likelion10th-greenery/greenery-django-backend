from django.db import models

# Create your models here.

class Tag(models.Model):
    """
    해시태그 모델
    """
    tag = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.tag
