from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import Adminshoppost
from products.models import Category, FoodProduct
from django.contrib.auth.models import User

def all_products_page(request):
    products = FoodProduct.objects.all()
    return render(request, "all-food.html", {"products":products})

def restaurant_profile(request, id):
    shop_instance = Adminshoppost.objects.get(id = id)
    restaurants = Adminshoppost.objects.all()

    products = FoodProduct.objects.filter(shop=shop_instance)
    #.order_by('id', 'shop_instance')

    return render(request, "shop_details_products.html", {"shop_details":shop_instance, "restaurants":restaurants, "products":products})
