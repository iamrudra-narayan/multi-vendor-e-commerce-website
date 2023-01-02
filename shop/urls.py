from django.contrib import admin
from django.urls import path,include
from shop import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    path("delivery/", views.delivery, name="delivery"),
    path("dining/", views.dining, name="dining"),
    path("delivery/order/<int:id>", views.hotel_products_page, name="hotel_products"),
    path("category/<str:prod_item>", views.category_products, name="category_products"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)