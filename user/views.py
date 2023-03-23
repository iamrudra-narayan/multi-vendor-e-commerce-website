from http.client import HTTPResponse
from django.shortcuts import render, redirect
from twilio.rest import Client
from django.contrib import messages
from django.contrib.auth.models import User
from user.models import Userprofile
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from .models import Address
from payment.models import Order
from .models import Adminshoppost

# Create your views here.

  
def register(request):
    if request.user.is_authenticated:
      return redirect("/")
    if request.method == "POST":
        try:
            email = request.POST['email']
            User.objects.get(username = request.POST['email'])
            messages.error(request, f"The Email {email} is already taken. Try a unique Email.")
            return redirect ('/myaccount/register/')
        except User.DoesNotExist:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User(username=email, first_name=fname, last_name=lname)
            user.set_password(password)
            user.save()
            messages.success(request, f"Registration Successful. Welcome {fname} {lname}. Please Login to Proceed.")
            return redirect('/myaccount/login/') 
    else:
        return render(request,'register.html')
       

def login(request):
    if request.user.is_authenticated:
      return redirect("/")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request, f"Welcome back {user.username}.")
            return redirect('/myaccount/profile/')
        else:
            messages.error(request, f"Invalid Credentials. Login again.")
            return redirect('/myaccount/login/')
    else:               
        return render(request, "login.html") 

@login_required(login_url='login')
def editprofile(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('email')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        user = User.objects.get(id = request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        user_details = Userprofile.objects.get(id = request.user.userprofile.id)
        user_details.age = age
        user_details.gender = gender
        user_details.save()

        messages.success(request, f"Profile Details updated successfully.")
        return redirect('/myaccount/profile/') 
    else:
        return render(request,'update-profile.html')


def logout_user(request):
	logout(request)
	return redirect("/myaccount/login/")

@login_required(login_url='login')
def profile(request):
    user_id = request.user.id
    user=User.objects.filter(id=user_id).first()
    address = Address.objects.filter(user = request.user)
    return render(request, "profile.html",{'user':user, 'address':address})   

@login_required(login_url='login')
def addprofile(request):
    if request.method == "POST":
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        user_instance = Userprofile.objects.get(id = request.user.id)
        user_details = user_instance(user=user_instance,age=age, gender=gender)
        user_details.save()

        messages.success(request, f"Profile Details updated successfully.")
        return redirect('/myaccount/profile/') 
    else:
        return render(request,'update-profile.html')


'''@login_required(login_url='login')
def update_pic(request):
    if request.method == "POST":
        picture = request.File["picture"]

        user_profile = Userprofile.objects.get(id = request.user.userprofile.id)
        user_profile.picture = picture
        user_profile.save()

        messages.success(request, f"Profile Picture updated successfully.")
        return redirect('/profile/')
    return render(request, "update-picture.html") '''

def new_add(request):
    if request.method == "POST":
        user =  request.user
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        s_mobile = request.POST.get('s_mobile')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        city = request.POST.get('city')
        dist = request.POST.get('district')
        state = request.POST.get('state')
        place = request.POST.get('place')

        address = Address(user=user, name=name, mobile=mobile, s_mobile=s_mobile, pincode=pincode, address=address, city=city, dist=dist, state=state, place=place)
        address.save()

        return redirect('profile')
    return render(request, "new_add.html")


def update_add(request, id):
    address = Address.objects.get(user = request.user)
    if request.method == "POST":
        user =  request.user
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        s_mobile = request.POST.get('s_mobile')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        city = request.POST.get('city')
        dist = request.POST.get('district')
        state = request.POST.get('state')
        place = request.POST.get('place')

        user_add = Address.objects.get(user = user)
        user_add.name = name
        user_add.mobile = mobile
        user_add.s_mobile = s_mobile
        user_add.pincode = pincode
        user_add.address  = address
        user_add.city = city
        user_add.dist = dist
        user_add.state = state
        user_add.place = place
        user_add.save()  

        return redirect('profile')
    return render(request, "update_add.html", {'address': address})   

@login_required(login_url='login')
def orders(request):
    user = request.user
    address = Address.objects.filter(user = request.user)
    orders = Order.objects.filter(user = user)
    print(orders)
    return render(request, "orders.html",{'user':user, 'address':address, 'orders':orders}) 

@login_required(login_url='login')
def order_details(request, order_id):
    user = request.user
    address = Address.objects.filter(user = user)
    orders = Order.objects.filter(order_id=order_id).first()
    ordered_items = orders.cart_items
    items = str(ordered_items)[1:-1]
    print(items)
    return render(request, "order-details.html",{'user':user, 'address':address, 'order_details':orders, 'items':items})        

'''{'1': {'userid': 2, 'product_id': 1, 'name': 'Chicken Dum Biriyani Half', 'quantity': 3, 'price': '99', 'image': '/media/pics/productimages/biriyani.jpg'},
 '2': {'userid': 2, 'product_id': 2, 'name': 'Egg Roll (Double Egg)', 'quantity': 5, 'price': '50', 'image': '/media/pics/productimages/eggroll.jpg'}}'''    