# Generated by Django 4.1.3 on 2023-02-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_qna_img_cnt_qna_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantdiary',
            name='book_mark',
        ),
        migrations.RemoveField(
            model_name='plantdiary',
            name='like',
        ),
        migrations.RemoveField(
            model_name='plantdiary',
            name='order',
        ),
        migrations.RemoveField(
            model_name='plantdiary',
            name='post_img',
        ),
        migrations.AddField(
            model_name='plantdiary',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='plantdiary',
            name='month',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='plantdiary',
            name='plantprofile',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='plantdiary',
            name='sun',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='plantdiary',
            name='water',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='plantdiary',
            name='year',
            field=models.IntegerField(default=2020),
        ),
        migrations.AlterField(
            model_name='plantdiary',
            name='img_url',
            field=models.TextField(blank=True, default='default_img', null=True),
        ),
    ]