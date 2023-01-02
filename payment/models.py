from django.db import models
from django.contrib.auth.models import User
from django.utils  import timezone
from user.models import Address
from products.models import FoodProduct

# Create your models here.
'''class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50, default="")
    pincode = models.IntegerField(default="")
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False, default="Choudwar")
    dist = models.CharField(max_length=100, blank=False, default="Cuttack")
    state = models.CharField(max_length=100, blank=False, default="Odisha")
    mobile = models.IntegerField(blank=False)
    s_mobile = models.IntegerField(blank=False)
    place = models.CharField(max_length=5, blank=False, default="")

    def __str__(self):
        return self.user.username + " " + str(self.address)'''


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    address = models.ForeignKey(Address, default= True, on_delete=models.CASCADE)
    cart_items =  models.CharField(max_length=2550, default=None)
    prod_price = models.FloatField(default=0)
    method = models.CharField(max_length=50, blank=False, default="Razorpay")
    quantity = models.IntegerField(blank=False, default=0)
    total_price = models.FloatField(blank=False, default=0)
    payment_status = models.BooleanField(default=True)
    order_id = models.CharField(unique=True, max_length=200, null=True, default=None) 
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    created_at = models.TimeField(auto_now=True, editable=False)
    razorpay_order_id = models.CharField(max_length=1000, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=1000, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user.username + " " + str(self.order_id)

    '''def save(self, *args, **kwargs):
            if self.order_id is None and self.datetime_of_payment:
                self.order_id = self.datetime_of_payment.strftime('ORDER%Y%m%dODR') 
                return super(Order,self).save(*args, **kwargs)'''

