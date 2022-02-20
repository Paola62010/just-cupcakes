from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.view_products, name='products'),
    path('<slug:slug>/', views.product_detail,
         name='product_detail'),
]
