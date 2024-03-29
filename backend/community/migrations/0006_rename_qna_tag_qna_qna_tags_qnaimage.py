# Generated by Django 4.1.3 on 2023-01-08 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_qna'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qna',
            old_name='qna_tag',
            new_name='qna_tags',
        ),
        migrations.CreateModel(
            name='QnAImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('qna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.qna')),
            ],
        ),
    ]
