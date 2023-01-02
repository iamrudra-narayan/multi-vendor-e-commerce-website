from django.shortcuts import render
import razorpay
from mysite.settings import RAZOR_KEY_ID, RAZOR_KEY_SECRET
from shop.views import *
from ecart.cart import Cart
from django.contrib.auth.decorators import login_required
from .models import Order
from django.http import HttpResponse
from ecart.views import cart_clear
from .models import Address
import random

client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

@login_required(login_url='login')
def payment(request):
    user = request.user.id
    user_instance = User.objects.get(id=user)
    address = Address.objects.filter(user=user_instance)
    print(address)

    cart = Cart(request)
    order_amount = (cart.total())*100
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'
    notes = {'Shiping address': 'Choudwar, Cuttack'}

    payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, receipt = order_receipt, notes=notes, payment_capture=1))
    payment_order_id = payment_order['id']

    context = {
        'amount': (order_amount)/100, 'RAZORPAY_KEY_ID': RAZOR_KEY_ID, 'order_id': payment_order_id, 'address': address,
    }
    return render(request, 'payment.html',context)


@login_required(login_url='login')
def success(request):
    cart_items = []
    cart = Cart(request)
    d_address = Address.objects.get(user=request.user)
    order_id = random.randint(100000,999999999999)
    total_price =  cart.total()
    razorpay_order_id = 12345
    razorpay_payment_id = 12345
    razorpay_signature = 12345
    carts = request.session.get('cart')
    print(carts)
    for i in carts:
        cart_item = carts[i]['name']
        print(cart_items)
        cart_items.append(cart_item)

    order = Order(user = request.user,cart_items=cart_items ,quantity=carts[i]['quantity'],prod_price=carts[i]['price'], address = d_address,total_price = total_price, order_id = order_id, razorpay_order_id=razorpay_order_id, razorpay_payment_id=razorpay_payment_id, razorpay_signature=razorpay_signature)
    order.save()

    request.session['cart'] = {}

    orders = Order.objects.filter(order_id=order_id).first()
    
    return render(request, 'success.html', {'order_details': orders})


@login_required(login_url='login')
def failed(request):
    return render(request, 'failed.html')   



'''@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            order_id = request.POST.get('razorpay_order_id','')
            signature = request.POST.get('razorpay_signature','')
            params_dict = { 
            'razorpay_order_id': order_id, 
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
            try:
                order_db = Order.objects.get(razorpay_order_id=order_id)
            except:
                return HttpResponse("505 Not Found")
            order_db.razorpay_payment_id = payment_id
            order_db.razorpay_signature = signature
            order_db.save()
            result = client.utility.verify_payment_signature(params_dict)
            if result==None:
                amount = order_db.total_amount * 100   #we have to pass in paisa
                try:
                    client.payment.capture(payment_id, amount)
                    order_db.payment_status = 1
                    order_db.save()
                    return render(request, 'firstapp/payment/paymentsuccess.html',{'id':order_db.id})
                except:
                    order_db.payment_status = 2
                    order_db.save()
                    return render(request, 'firstapp/payment/paymentfailed.html')
            else:
                order_db.payment_status = 2
                order_db.save()'''    
