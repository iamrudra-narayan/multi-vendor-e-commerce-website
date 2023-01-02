from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import Adminshoppost
from products.models import Category, FoodProduct
from django.contrib.auth.models import User
from shop.models import Cart


# Create your views here.

def delivery(request):
    categories = Category.objects.all()
    restaurants = Adminshoppost.objects.all()
    return render(request, "delivery.html", {"categories":categories, "restaurants":restaurants})

def dining(request):
    return render(request, "dining.html")   

def hotel_products_page(request, id):
    shop_instance = Adminshoppost.objects.get(id = id)
    restaurants = Adminshoppost.objects.all()
    
    products = FoodProduct.objects.filter(shop=shop_instance)
    #.order_by('id', 'shop_instance')


    return render(request, "shop_details_products.html", {"shop_details":shop_instance, "restaurants":restaurants, "products":products})    

def category_products(request, prod_item):
    category_instance = Category.objects.get(prod_item = prod_item)
    products = FoodProduct.objects.filter(prod_category = category_instance)            

    return render(request, "category_products.html", {"products":products,"category_name":category_instance})

    
   


