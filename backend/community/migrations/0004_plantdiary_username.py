# Generated by Django 4.1.3 on 2022-12-03 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_plantdiary_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantdiary',
            name='username',
            field=models.CharField(default='비회원', max_length=50),
        ),
    ]
