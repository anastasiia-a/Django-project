# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.shortcuts import render

from .models import Category, Product
from .functions import list_category, get_pages, get_parents


def index(request):
    all_product = Product.objects.all()
    all_category = list_category(get_parents(Category))
    page, product = get_pages(request, all_product, 3)

    context = {'all_product': product, 'page': page, 'all_category': all_category}
    return render(request, 'catalog/list.html', context)


def prod_id(request):
    all_category = list_category(get_parents(Category))
    request_path = re.split(r'/',  str(request.get_full_path()))
    request_id = int(request_path[-1])
    prod = Product.objects.filter(id=request_id)

    context = {'prod': prod[0], 'all_category': all_category}
    return render(request, 'catalog/prod.html', context)


def products(request, slug):
    category = re.split(r'/', str(slug))

    if len(category) != 1:
        category = str(category[-1])
    else:
        category = category[0]

    category = Category.objects.filter(slug=category)
    selected = category
    suitable_category = list_category(category)
    prod = []

    for category in suitable_category:
        for product in Product.objects.filter(feature_prod=category):
            prod.append(product)

    all_category = list_category(get_parents(Category))
    page, product = get_pages(request, prod, 1)

    context = {'all_product': product, 'page': page, 'all_category': all_category, 'selected': selected[0]}
    return render(request, 'catalog/list.html', context)

