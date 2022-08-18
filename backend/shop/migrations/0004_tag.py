# Generated by Django 4.0.4 on 2022-08-18 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_plant_pub_date_alter_plant_deliver_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField()),
                ('plant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.plant')),
            ],
        ),
    ]