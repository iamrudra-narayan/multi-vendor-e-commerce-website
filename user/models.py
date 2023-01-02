from django.db import models
from django.contrib.auth.models import User
from django.utils  import timezone

# Create your models here.

#Admin Control Models    
class Userprofile(models.Model):   
    age = models.CharField(max_length=3, default="Null")
    gender = models.CharField(max_length=8, default="Null")
    user_model = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.user_model.username)

class Adminshoppost(models.Model):  
    shop_name = models.CharField(max_length=30, default="name")
    shop_banner = models.ImageField(upload_to="pics/shopbanner", default="")
    shop_details = models.TextField(max_length=300, default="")
    shop_address = models.TextField(max_length=100, default="")
    mobile = models.CharField(max_length=13, default="")
    email = models.EmailField(max_length=30, default="")   
    open_time = models.TextField(max_length=6, default="11AM") 
    close_time = models.TextField(max_length=6, default="10PM") 
    open_status = models.BooleanField(default="")

    def __str__(self):
        return (self.shop_name)

class Address(models.Model):
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
        return self.user.username + " " + str(self.address)        

                