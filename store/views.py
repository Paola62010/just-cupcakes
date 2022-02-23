from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.db.models.functions import Lower


def home(request):
    """A view to render the home page"""
    return render(request, 'index.html')


def view_products(request):
    """A view to show all available products"""

    products = Product.objects.all()
    query = None
    categories = None
    current_sorting = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            result = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(result)

        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__slug=categories)
            categories = Category.objects.filter(slug=categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search': query,
        'current_category': categories,
        'current_sorting': current_sorting
    }
    return render(request, 'products.html', context)


def product_detail(request, slug):
    """A view to show the product details"""

    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
