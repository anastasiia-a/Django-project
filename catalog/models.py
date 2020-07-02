# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def get_tree(category):
    list_parents = []

    def recursions(obj):
        list_parents.append(obj.slug)

        while (obj.parent is not None):
            return recursions(obj.parent)

    recursions(category)
    return list_parents[::-1]


class Category(models.Model):
    name = models.CharField('Category', max_length=250)
    slug = models.SlugField(max_length=50)
    img_category = models.ImageField(upload_to='img/')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_slug(self):
        all_objects = get_tree(self)
        slug = '/'.join(all_objects)
        return str(slug)


class Product(models.Model):
    feature_prod = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_category')
    slug = models.SlugField(default='prod_id')
    name_prod = models.CharField('Name Product', max_length=200)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name_prod

    def get_slug(self):
        return str(self.slug)


