# Generated by Django 4.0.4 on 2022-12-03 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_img',
            field=models.TextField(default='greenary', max_length=100),
        ),
    ]
