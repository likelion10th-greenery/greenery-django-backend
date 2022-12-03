from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Community(models.Model):
    post_img = models.TextField(blank=True, null=True)

class Comment(models.Model):
    post = models.ForeignKey(PlantDiary, related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    body = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)