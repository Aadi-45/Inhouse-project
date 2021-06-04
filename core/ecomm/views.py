from django.shortcuts import render, redirect
from .models import Product

def homeView(request):
    context = {}
    return render(request, 'ecomm/index.html', context)

def product_view(request, id):
    prod = Product.objects.get(id = id)
    context = {
        'prod': prod,
    }
    return render(request, 'ecomm/product.html', context)

