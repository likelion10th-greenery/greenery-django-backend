# Generated by Django 4.0.6 on 2022-09-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_tag_plant_plant_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
