from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=30, default="") 
    email = models.EmailField(max_length=30, default="")
    subject = models.CharField(max_length=300, default="")
    message = models.CharField(max_length=3000, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.user)