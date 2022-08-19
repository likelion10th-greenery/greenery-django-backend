# Generated by Django 4.1 on 2022-08-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_customuser_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
