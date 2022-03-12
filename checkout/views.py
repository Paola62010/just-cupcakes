from re import template
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Order, LineItem
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag yet.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
