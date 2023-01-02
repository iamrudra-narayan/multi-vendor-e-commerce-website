from django.db import models
from django.contrib.auth.models import User
from user.models import Adminshoppost


class Category(models.Model):
    food_category = models.CharField(max_length=40, default="Non-Veg") 
    prod_item = models.CharField(max_length=40, default="Biriyani") 
    category_image = models.ImageField(upload_to="pics/categoryimages", default="")
    def __str__(self):
        return (self.prod_item) 

class FoodProduct(models.Model):
    prod_name = models.CharField(max_length=30, default="Product") 
    prod_image = models.ImageField(upload_to="pics/productimages", default="")
    prod_desc = models.TextField(max_length=30, default="")
    marked_price = models.IntegerField()
    discount_price = models.IntegerField()
    selling_price = models.IntegerField()   
    item_availability = models.BooleanField(default="") 
    created_at = models.DateTimeField(auto_now=True)
    prod_category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    shop = models.ForeignKey(Adminshoppost, on_delete=models.CASCADE)

    def __str__(self):
        return (self.prod_name)
