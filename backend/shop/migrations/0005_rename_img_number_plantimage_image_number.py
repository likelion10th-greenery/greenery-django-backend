# Generated by Django 4.0.6 on 2022-08-18 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_plant_pic1_remove_plant_pic10_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantimage',
            old_name='img_number',
            new_name='image_number',
        ),
    ]