from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from store.models import Product
from django.contrib import messages
from django.urls import reverse


def view_bag(request):
    """A view to render the bag page"""
    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    """A view to add products to the shopping bag"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)


def bag_remove(request, item_id):
    """A view to remove items from the bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return redirect(reverse('bag'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect(reverse('bag'))


def bag_edit(request, item_id):
    """A view to edit the bag items quantity"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {bag[item_id]}'))
    return redirect(reverse('bag'))
