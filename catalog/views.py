# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Category, Product
from .functions import all_children, get_pages, all_parents, get_tree


def index(request):
    all_product = Product.objects.all()
    all_category = get_tree(Category.objects.all())
    product = get_pages(request, all_product, 3)

    context = {'all_product': product, 'all_category': all_category, 'page': product}
    return render(request, 'catalog/list.html', context)


def prod_id(request):
    categories = Category.objects.all()
    all_category = get_tree(categories)
    request_path = re.split(r'/',  str(request.get_full_path()))
    request_id = int(request_path[-1])
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

    return HttpResponse("Page not found")


def search(request):
    get_search = request.POST.get('search')

    prod = Product.objects.filter(
        Q(name_prod__icontains=get_search) | Q(text__icontains=get_search)
    )

    all_category = get_tree(Category.objects.all())
    product = get_pages(request, prod, 1)

    context = {'all_product': product, 'all_category': all_category, 'page': product}

    html = render_to_string('blockcontent.html', context=context)
    return JsonResponse({'html': html})


def products(request, slug):
    categories = Category.objects.all()
    category = re.split(r'/', str(slug))

    if len(category) != 1:
        category = str(category[-1])
    else:
        category = category[0]

    category = Category.objects.filter(slug=category)
    selected = category[0]
    address = all_parents(category[0], categories)

    prod = []
    for category in all_children(category, categories):
        for product in Product.objects.filter(feature_prod=category):
            prod.append(product)

    product = get_pages(request, prod, 1)
    context = {'all_product': product, 'all_category': get_tree(categories),
               'selected': selected, 'address': address, 'page': product}

    html = render_to_string('blockcontent.html', context=context)

    if request.method == 'POST':
        return JsonResponse({'html': html})
    return render(request, 'catalog/list.html', context)

