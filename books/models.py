# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):

    CATEGORY = (
        ('Classic','Classic'),
        ('Horror','Horror'),
        ('Novel','Novel'),
        ('Sci-Fi','Sci-Fi'),
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=200, choices=CATEGORY)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Books'
