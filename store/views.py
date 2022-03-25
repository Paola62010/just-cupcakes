from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product, Category
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProductForm


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
        'product': product,
    }
    return render(request, 'product_detail.html', context)


@login_required
def add_product(request):
    """View to add a new product"""
    if not request.user.is_superuser:
        messages.error(request, ('Sorry, you do not have '
                                 'privileges to access this '
                                 'page.'))
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully.')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request,
                           ('Sorry, your product coult not be added. '
                            'Make sure the entered information is '
                            'valid.'))
    else:
        form = ProductForm()

    template = 'add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, slug):
    """View to edit an existing product"""
    if not request.user.is_superuser:
        messages.error(request, ('Sorry, you do not have '
                                 'privileges to access this '
                                 'page.'))
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request,
                           ('Sorry, your product coult not be updated. '
                            'Make sure the entered information is '
                            'valid.'))
    else:
        form = ProductForm(instance=product)

    template = 'edit_product.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)
