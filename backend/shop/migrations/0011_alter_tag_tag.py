# Generated by Django 4.0.6 on 2022-09-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_plant_plant_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]