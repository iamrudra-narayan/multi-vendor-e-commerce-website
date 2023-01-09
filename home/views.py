from http.client import HTTPResponse
from django.shortcuts import render, redirect
from twilio.rest import Client
from django.contrib import messages
from products.models import Category,FoodProduct
from user.models import Adminshoppost
from django.db.models import Q
from .models import ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request): 
    if request.method == 'POST':
        phno = request.POST.get('phno')
        account_sid = 'AC1377db0737256c348fc40a77e5f15a2c' 
        auth_token = '713072aa418475034bcccc3b247d901c' 
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

@login_required(login_url='login')
def contactUs(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('sub')
        message = request.POST.get('msg')

        contact = ContactForm(name=name, email=email, subject=subject, message=message, user=request.user)
        contact.save()
        messages.success(request, f'Thanks for contacting us. We will be reply to you as soon as possible!')
        return redirect('contact')

    return render(request, 'contact.html')

@login_required(login_url='login')
def notifications(request): 
    return render(request, 'notifications.html')

@login_required(login_url='login')
def favourites(request): 
    return render(request, 'favourites.html')    

