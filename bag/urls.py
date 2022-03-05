from django.urls import path
from . import views

urlpatterns = [
    path('bag', views.view_bag, name='bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<item_id>/', views.bag_remove, name='bag_remove'),
    path('edit/<item_id>/', views.bag_edit, name='bag_edit'),
]
