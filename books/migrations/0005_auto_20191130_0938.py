# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-30 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20191129_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(height_field=300, upload_to='uploaded_img/', width_field=210),
        ),
    ]
