from django.contrib import admin
from django.urls import path,include
from products import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    path("delivery-items/", views.all_products_page, name="delivery-items"),
    path("order/<int:id>", views.restaurant_profile, name="hotel_profile"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)