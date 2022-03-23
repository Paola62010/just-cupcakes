import email
import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from store.models import Product
from django_countries.fields import CountryField


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    address_line1 = models.CharField(max_length=80, null=False, blank=False)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=80, null=False, blank=False)
    country = CountryField(blank_label='Country *', max_length=20, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _create_order_number(self):
        """Generate a random order ID"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Updates grand total when line items are added"""
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kargs):
        """
        Override original save method and
        generates an order ID if it wasn't already generated
        """
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kargs)

    def __str__(self):
        return self.order_number


class LineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kargs):
        """
        Overrides original ave method to set
        lineitem total and update order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
