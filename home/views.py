from http.client import HTTPResponse
from django.shortcuts import render, redirect
from twilio.rest import Client
from django.contrib import messages
from products.models import Category,FoodProduct
from user.models import Adminshoppost
from django.db.models import Q

# Create your views here.

def home(request): 
    if request.method == 'POST':
        phno = request.POST.get('phno')
        account_sid = 'AC1377db0737256c348fc40a77e5f15a2c' 
        auth_token = '329661f26c0c8780d621af592a0c6860' 
        client = Client(account_sid, auth_token) 
 
        client.messages.create(
                              from_='+12342316600',
                              body ='''Thank you for using Zomato.\n
                              Download the Zomato app using link below:\n

                              Android- https://play.google.com/store/apps/details?id=com.application.zomato&gl=US\n
                              
                              IOS- https://apps.apple.com/in/app/zomato-food-restaurants/id434613896''',
                              to ='+91'+phno
                          )
        messages.success(request, f"Link for App has been send Successfully to the mobile no. {'+91'+phno}.")
        return redirect("/")

    return render(request, "home.html")
   

def search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'
            return redirect("/")

        #results = FoodProduct.objects.filter(Q(prod_name__icontains=query) | Q(prod_desc__icontains=query))
        results = FoodProduct.objects.filter(prod_name__icontains=query)
        shop_results = Adminshoppost.objects.filter(shop_name__icontains=query)
        item_results = Category.objects.filter(food_category__icontains=query)

    return render(request, 'search-results.html', {'query': query, 'results': results, 'shop_results': shop_results, 'item_results': item_results})   
