from django.http import HttpResponse
from django.template.loader import render_to_string

import products
from shops.models import Shop
from categories.models import Category


def show_main_page(request):
    shops = Shop.objects.order_by('-id') [:5]
    categories = Category.objects.all() [:5]

    result = render_to_string('Svetoy1/svetoy1.html',
        {
        'categories': categories,
        'shops': shops,
        'products': products,})
    return HttpResponse(result)
def show_products(request):
    shops = Shop.objects.order_by('-id') [:5]
    categories = Category.objects.all() [:5]

    result = render_to_string('Svetoy1/svetoy3.html',
        {
        'categories': categories,
        'shops': shops,
        'products': products,})
    return HttpResponse(result)