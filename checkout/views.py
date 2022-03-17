from re import template
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from .models import Order, LineItem
from .forms import OrderForm
from bag.contexts import bag_content
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag yet.')
        return redirect(reverse('products'))

    current_bag = bag_content(request)
    order_total = current_bag['grand_total']
    stripe_total = round(order_total * 100)
    stripe.api_key = stripe_secret_key
    payment_intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    print(payment_intent)

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': payment_intent.client_secret
    }

    return render(request, template, context)
