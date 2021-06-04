from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def homeView(request):
    context = {}
    return render(request, 'ecomm/index.html', context)

def product_view(request, id):
    prod = Product.objects.get(id = id)
    context = {
        'prod': prod,
    }

    return render(request, 'ecomm/product.html', context)
@login_required 
def test_view(request):
    context = {}
    return render(request,"ecomm/personal.html",context)

