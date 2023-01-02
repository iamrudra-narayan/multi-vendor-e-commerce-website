from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    path("", views.payment, name="payment"),
    path("success/", views.success, name="success"),
    path("failed/", views.failed, name="failed"),
] 