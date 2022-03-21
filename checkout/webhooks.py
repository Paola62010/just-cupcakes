from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import stripe


class StripeWebhookHandler:
    """Handles Stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handles generic webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["event"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handles payment_intent.succeeded webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["event"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handles payment_intent.failed webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["event"]}',
            status=200
        )


@require_POST
@csrf_exempt
def webhook(request):
    """Listens for webhooks from Stripe"""
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    print('Success')
    return HttpResponse(status=200)
