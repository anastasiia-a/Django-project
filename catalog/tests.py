# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from catalog.models import Category


class SimpleTest(TestCase):
    def setUp(self):
        cat_root = Category.objects.create(name='Test1', slug='test1', img_category='img/test1.png')
        for num in range(3):
            Category.objects.create(name='Test_ch%s' % num, slug='test_ch%s' % num, img_category='img/test_ch%s.png' % num, parent=cat_root)

    def test_parent_queries(self):
        cat = Category.objects.filter(parent__isnull=False).select_related('parent').last()
        with self.assertNumQueries(0):
            print cat, cat.parent

    def test_child_queries(self):
        cat = Category.objects.filter(parent__isnull=True).prefetch_related('children').last()
        with self.assertNumQueries(0):
            print cat, cat.children.all()

