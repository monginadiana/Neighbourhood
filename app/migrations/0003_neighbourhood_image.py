# Generated by Django 3.0.8 on 2022-01-05 05:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220105_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
