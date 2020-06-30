# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Category, Product
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import re

def index(request):
    all_product = Product.objects.all()

    parent = []
    category = Category.objects.all()
    child = []
    for i in category:
        if (i == i.parent) | (i.parent == None):
            parent.append(i)
        else:
            child.append(i)

    print(parent)
    print(child)
    paginator = Paginator(all_product, 12)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    return render(request, 'catalog/list.html',
                  {'all_product': product, 'page': page, 'parent': parent, 'child': child})

def id(request):
    parent = []
    category = Category.objects.all()
    child = []
    for i in category:
        if (i==i.parent) | (i.parent == None):
            parent.append(i)
        else:
            child.append(i)

    request_path = re.split(r'/',  str(request.get_full_path()))
    request_id = int(request_path[-1])
    prod = Product.objects.filter(id=request_id)
    print(prod[0])
    return render(request, 'catalog/prod.html',
                  {'prod': prod[0], 'parent': parent, 'child': child})

def filter(request):
    request_path = re.split(r'/', str(request.get_full_path()))
    request_name = str(request_path[-1])
    product = Product.object.filter(feature_prod=request_name)
    print(product)

# def tree(root):
#     if (root.name==root.parent) | (root.parent == None):
#         return root

# Create your views here.
