# Generated by Django 4.1.3 on 2022-12-03 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_plantdiary_delete_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantdiary',
            name='title',
            field=models.CharField(default='제목 없음', max_length=100),
        ),
    ]
