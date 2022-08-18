from django.contrib import admin
from .models import Plant, PlantImage, Tag, PlantType

# Register your models here.

admin.site.register(Plant)
admin.site.register(PlantImage)
admin.site.register(Tag)
admin.site.register(PlantType)

