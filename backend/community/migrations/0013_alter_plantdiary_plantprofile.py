# Generated by Django 4.1.3 on 2023-02-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_alter_plantdiary_category_alter_plantdiary_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantdiary',
            name='plantprofile',
            field=models.CharField(default='선택 안 함', max_length=50),
        ),
    ]
