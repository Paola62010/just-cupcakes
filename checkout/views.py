from re import template
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from .models import Order, LineItem
from store.models import Product
from .forms import OrderForm
from bag.contexts import bag_content
import stripe


def checkout(request):
    """A view to handle the checkout form"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'city': request.POST['city'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'post_code': request.POST['post_code'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in bag.items():
                product = Product.objects.get(id=item_id)
                line_item = LineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                line_item.save()
            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse
                            ('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
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
        order_form = OrderForm()

    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': payment_intent.client_secret
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """View to handle successful checkout"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order created successfully! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    if 'bag' in request.session:
        del request.session['bag']
    template = 'checkout_success.html'
    context = {
        'order': order
    }

    return render(request, template, context)
