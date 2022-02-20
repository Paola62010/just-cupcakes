from django.shortcuts import render
from .models import Product, Category


def home(request):
    """A view to render the home page"""
    return render(request, 'index.html')


def view_products(request):
    """A view to show all available products"""

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)
