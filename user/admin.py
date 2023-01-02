from django.contrib import admin

# Register your models here.
from django.contrib import admin
from user.models import Userprofile, Adminshoppost
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Userprofile)