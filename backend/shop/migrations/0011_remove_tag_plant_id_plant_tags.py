# Generated by Django 4.0.6 on 2022-08-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_planttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='plant_id',
        ),
        migrations.AddField(
            model_name='plant',
            name='tags',
            field=models.ManyToManyField(blank=True, to='shop.tag'),
        ),
    ]