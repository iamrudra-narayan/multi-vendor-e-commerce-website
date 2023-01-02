from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import Adminshoppost
from products.models import FoodProduct
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
@login_required(login_url='login')
def cart(request):  
    cart = Cart(request)
    if request.method == 'POST':
        code = request.POST.get('promocode')
        print(code)
        promocode = "RUDRA93370"
        if code != promocode:
            messages.error(request, f"Promo code {code} is either invalid or expired!")
        else:
            amount = (cart.total() - 50)
            messages.success(request, f"Promo code {code} apply successfully! You get a discount of 50rs.")

    return render(request, "cart.html")    

@login_required(login_url='login')
def cart_add(request, id):
    cart = Cart(request)
    product = FoodProduct.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url='login')
def item_clear(request, id):
    cart = Cart(request)
    product = FoodProduct.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url='login')
def item_increment(request, id):
    cart = Cart(request)
    product = FoodProduct.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url='login')
def item_decrement(request, id):
    cart = Cart(request)
    product = FoodProduct.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url='login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")

    
