# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Category, Product
from .functions import list_category, get_dict


def index(request):
    all_product = Product.objects.all()

    parents = []
    categories = Category.objects.all()

    for category in categories:
        if category.parent is None:
            parents.append(category)

    print(list_category(parents))
    dict_category = get_dict(list_category(parents))
    print(dict_category)
    paginator = Paginator(all_product, 2)
    page = request.GET.get('page')

    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    context = {'all_product': product, 'page': page, 'all_category': dict_category}
    return render(request, 'catalog/list.html', context)


def prod_id(request):
    parents = []
    categories = Category.objects.all()

    for category in categories:
        if category.parent is None:
            parents.append(category)

    dict_category = get_dict(list_category(parents))
    request_path = re.split(r'/',  str(request.get_full_path()))
    request_id = int(request_path[-1])
    prod = Product.objects.filter(id=request_id)

    context = {'prod': prod[0], 'all_category': dict_category}
    return render(request, 'catalog/prod.html', context)


# def filter(request):
#     request_path = re.split(r'/', str(request.get_full_path()))
#     request_name = str(request_path[-1])
#     product = Product.objects.filter(feature_prod=request_name)
#     print(product)

