# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.shortcuts import render, HttpResponse
from django.db.models import Q

from .models import Category, Product
from .functions import all_children, get_pages, all_parents, get_tree


def index(request):
    all_product = Product.objects.all()
    all_category = get_tree(Category.objects.all())
    page, product = get_pages(request, all_product, 3)

    context = {'all_product': product, 'page': page, 'all_category': all_category}
    return render(request, 'catalog/list.html', context)


def prod_id(request):
    categories = Category.objects.all()
    all_category = get_tree(categories)
    request_path = re.split(r'/',  str(request.get_full_path()))
    request_id = int(request_path[-1])

    prod = Product.objects.filter(id=request_id)
    if prod:
        address = all_parents(prod[0].feature_prod, categories)
        context = {'prod': prod[0], 'all_category': all_category, 'address': address}
        return render(request, 'catalog/prod.html', context)

    return HttpResponse("Page not found")


def search(request):
    get_search = ''

    if request.method == "GET":
        if 'search' in request.GET:
            get_search = str(request.GET["search"]).lower()

    if get_search != '':
        prod = Product.objects.filter(
            Q(name_prod__icontains=get_search) | Q(text__icontains=get_search)
        )

        all_category = get_tree(Category.objects.all())
        page, product = get_pages(request, prod, 1)

        context = {'all_product': product, 'page': page,
                   'all_category': all_category}
        return render(request, 'catalog/list.html', context)

    return index(request)


def products(request, slug):
    categories = Category.objects.all()
    products = Product.objects.all()
    category = re.split(r'/', str(slug))

    if len(category) != 1:
        category = str(category[-1])
    else:
        category = category[0]

    category = Category.objects.filter(slug=category)
    selected = category[0]
    suitable_category = all_children(category, categories)
    address = all_parents(selected, categories)

    prod = []
    for category in suitable_category:
        for product in Product.objects.filter(feature_prod=category):
            prod.append(product)

    all_category = get_tree(Category.objects.all())
    page, product = get_pages(request, prod, 3)

    context = {'all_product': product, 'page': page,
               'all_category': all_category, 'selected': selected, 'address': address}
    return render(request, 'catalog/list.html', context)

