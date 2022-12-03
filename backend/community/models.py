from django.db import models

# Create your models here.

class Community(models.Model):
    post_img = models.TextField(blank=True, null=True)