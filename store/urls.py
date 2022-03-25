from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.view_products, name='products'),
    path('products/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<slug:slug>/', views.edit_product, name='edit_product'),
]
