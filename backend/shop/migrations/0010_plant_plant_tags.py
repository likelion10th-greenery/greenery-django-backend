# Generated by Django 4.0.6 on 2022-09-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_plant_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='plant_tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]