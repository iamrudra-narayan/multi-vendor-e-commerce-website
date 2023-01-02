from django.db import models
from django.contrib.auth.models import User
from products.models import FoodProduct


class Cart(models.Model): 
    food = models.ForeignKey(FoodProduct, on_delete=models.CASCADE, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    def __str__(self):
        return (self.user.username) 
