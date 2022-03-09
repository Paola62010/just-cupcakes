from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import LineItem


@receiver(post_save, sender=LineItem)
def update_on_save(sender, instance, created, **kwargs):
    """Updates total on line item creation/update"""
    instance.order.update_total()


@receiver(post_delete, sender=LineItem)
def update_on_delete(sender, instance, **kwargs):
    """Updates total on line item removal"""
    instance.order.update_total()
