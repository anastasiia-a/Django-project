# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .functions import all_parents


class Category(models.Model):
    name = models.CharField('Category', max_length=250)
    slug = models.SlugField(max_length=50)
    img_category = models.ImageField(upload_to='img/')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        all_objects = all_parents(self, Category.objects.all(), type_list='slug')
        slug = '/'.join(all_objects)
        return '/%s' % str(slug)

    def count_spaces(self):
        spaces = []

        slug = self.get_absolute_url()
        for _ in range(slug.count('/')):
            spaces.append('')

        return spaces


class Product(models.Model):
    feature_prod = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_category')
    name_prod = models.CharField('Name Product', max_length=200)
    image = models.ImageField(upload_to='img/')
    text = models.TextField(null=True)

    def __str__(self):
        return self.name_prod

    def get_absolute_url(self):
        return str('/prod_id/%s' % self.id)


