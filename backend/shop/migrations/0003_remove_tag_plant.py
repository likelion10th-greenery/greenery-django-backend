# Generated by Django 4.0.6 on 2022-09-24 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_tag_practice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='plant',
        ),
    ]
