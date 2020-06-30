# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

class Category(models.Model):
    name = models.CharField('Category', max_length=250)
    img_category = models.ImageField(upload_to='img/')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    feature_prod = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_prod')
    name_prod = models.CharField('Name Product', max_length=200)
    image = models.ImageField(upload_to='img/')


    def __str__(self):
        return self.name_prod

