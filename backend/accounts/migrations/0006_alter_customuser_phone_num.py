# Generated by Django 4.1 on 2022-08-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_phone_num_customuser_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_num',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]