# Generated by Django 4.1.3 on 2023-02-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_remove_plantdiary_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantdiary',
            name='body',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
