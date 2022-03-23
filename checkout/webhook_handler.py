from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from store.models import Product
from .models import LineItem, Order
import stripe
import json
import time

class StripeWebhookHandler:
    """Handles Stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handles generic webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handles payment_intent.succeeded webhook"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    post_code__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    address_line1__iexact=shipping_details.address.line1,
                    address_line2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                        content=(f'Webhook received:{event["type"]} | SUCCESS:'
                                 'Verified order already in database'),
                        status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    post_code=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    address_line1=shipping_details.address.line1,
                    address_line2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, quantity in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    line_item = LineItem(
                        order=order,
                        product=product,
                        quantity=quantity
                    )
                    line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        print(intent)
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order via webhook'),
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handles payment_intent.failed webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
