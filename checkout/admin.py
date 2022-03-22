from django.contrib import admin
from .models import Order, LineItem


class LineItemAdminInline(admin.TabularInline):
    model = LineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (LineItemAdminInline,)
    readonly_fields = ('order_number', 'order_date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')
    fields = ('order_number', 'full_name', 'email',
              'phone', 'city', 'address_line1',
              'address_line2', 'post_code', 'county',
              'country', 'order_date', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')
    list_display = ('order_number', 'full_name', 'order_date',
                    'delivery_cost', 'order_total', 'grand_total')
    ordering = ('-order_date',)
