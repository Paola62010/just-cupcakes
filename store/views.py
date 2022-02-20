from django.shortcuts import render, get_object_or_404
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


def product_detail(request, slug):
    """A view to show the product details"""

    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
