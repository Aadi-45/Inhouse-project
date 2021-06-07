from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.views import loginView
from accounts.forms import UserProfileForm, SignUpForm

def homeView(request):
    context = {}
    return render(request, 'ecomm/index.html', context)

def productView(request, id):
    if request.method == 'POST':
        to_cart = request.POST.get('to_cart')
        rem_cart = request.POST.get('rem_cart')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(to_cart)
            if quantity:
                if rem_cart:
                    if quantity <= 1:
                        cart.pop(to_cart)
                    else:
                        cart[to_cart] = quantity-1
                else:
                    cart[to_cart] = quantity+1
            else:
                cart[to_cart] = 1
        else:
            cart = {}
            cart[to_cart] = 1
        request.session['cart'] = cart
        print(request.session['cart'])

    prod = Product.objects.get(id = id)
    context = {
        'prod': prod,
    }

    return render(request, 'ecomm/product.html', context)

@login_required
def cartView(request):
    if request.method == 'POST':
        to_cart = request.POST.get('to_cart')
        cart = request.session.get('cart')
        cart.pop(str(to_cart))
        request.session['cart']=cart
    ids = list(request.session.get('cart').keys())
    products = Product.get_product_by_id(ids)
    context={
        'cart_prod':products
    }
    return render(request, "ecomm/cart.html", context)

@login_required 
def profileView(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    context = {
        "form" : form
    }
    return render(request,"ecomm/profile.html",context)

