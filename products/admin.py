from django.contrib import admin

# Register your models here.
from django.contrib import admin
from products.models import Category, FoodProduct
from user.models import Adminshoppost
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Adminshoppost)
admin.site.register(Category)
admin.site.register(FoodProduct)
