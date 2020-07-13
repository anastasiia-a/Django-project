# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse
from rest_framework import status

from .models import Category, Product
from .functions import all_children, get_pages, all_parents, get_tree


def prod_id(request):
    categories = Category.objects.all()
    all_category = get_tree(categories)
    request_path = re.split(r'/',  str(request.get_full_path()))
    try:
        request_id = int(request_path[-1])
    except ValueError:
        request_id = 0

    prod = Product.objects.filter(id=request_id)
    product_pages = get_pages(request, prod, 1)

    if prod:
        address = all_parents(prod[0].feature_prod, categories)
        context = {'all_product': prod, 'all_category': all_category,
                   'address': address, 'text': 'text', 'page': product_pages}

        html = render_to_string('blockcontent.html', context=context)

        if request.method == 'POST':
            return JsonResponse({'html': html})
        return render(request, 'catalog/list.html', context)

    return render(request, 'catalog/404.html')


def search(request):
    if request.is_ajax():
        get_search = request.GET.get('search')
    else:
        get_search = re.findall(r'/search/([\w|.|/|-|_]{1,})', request.get_full_path())
        get_search = get_search[0]

    prod = Product.objects.filter(
        Q(name_prod__icontains=get_search) | Q(text__icontains=get_search)
    )

    all_category = get_tree(Category.objects.all())
    product = get_pages(request, prod, 1)
    context = {'all_product': product, 'all_category': all_category, 'page': product}
    html = render_to_string('blockcontent.html', context=context)

    if request.is_ajax():
        return JsonResponse({'html': html})

    return render(request, 'catalog/list.html', context)


def products(request, slug):
    categories = Category.objects.all()

    if slug != '':
        category = re.split(r'/', str(slug))
        category = category[-1]
        print(category)

        if Category.objects.filter(slug=category):
            category = Category.objects.filter(slug=category)
        else:
            return render(request, 'catalog/404.html')

        prod = []
        for cat in all_children(category, categories):
            for product in Product.objects.filter(feature_prod=cat):
                prod.append(product)

        product = get_pages(request, prod, 1)
        context = {'all_product': product, 'all_category': get_tree(categories),
                   'selected': category[0],
                   'address': all_parents(category[0], categories),
                   'page': product}
    else:
        product = get_pages(request, Product.objects.all(), 3)
        context = {'all_product': product,
                   'all_category': get_tree(categories),
                   'page': product}

    html = render_to_string('blockcontent.html', context=context)

    if (request.method == 'POST') | (request.is_ajax()):
        return JsonResponse({'html': html})
    return render(request, 'catalog/list.html', context)

