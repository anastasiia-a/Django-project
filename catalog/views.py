# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Category, Product


def index(request):
    all_product = Product.objects.all()

    parent = []
    category = Category.objects.all()
    child = []
    for i in category:
        if (i == i.parent) | (i.parent is None):
            parent.append(i)
        else:
            child.append(i)

    print(parent)
    print(child)
    paginator = Paginator(all_product, 2)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    context = {'all_product': product, 'page': page, 'parent': parent, 'child': child}
    return render(request, 'catalog/list.html', context)


def id(request):
    parent = []
    category = Category.objects.all()
    child = []
    for i in category:
        if (i == i.parent) | (i.parent is None):
            parent.append(i)
        else:
            child.append(i)

    request_path = re.split(r'/',  str(request.get_full_path()))
    request_id = int(request_path[-1])
    prod = Product.objects.filter(id=request_id)
    print(prod[0])
    context = {'prod': prod[0], 'parent': parent, 'child': child}
    return render(request, 'catalog/prod.html', context)


def filter(request):
    request_path = re.split(r'/', str(request.get_full_path()))
    request_name = str(request_path[-1])
    product = Product.objects.filter(feature_prod=request_name)
    print(product)

# def tree(root):
#     if (root.name==root.parent) | (root.parent == None):
#         return root

# Create your views here.
