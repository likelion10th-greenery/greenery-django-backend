# Generated by Django 4.0.6 on 2022-09-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_tag_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='plant',
            field=models.ManyToManyField(to='shop.plant'),
        ),
    ]
