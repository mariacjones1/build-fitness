# Generated by Django 3.2.20 on 2023-08-19 10:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_auto_20230818_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
