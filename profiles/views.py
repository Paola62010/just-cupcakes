from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


@login_required
def view_profile(request):
    """Displays the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    template = 'profile.html'
    context = {
        'orders': orders,
        'profile': profile
    }

    return render(request, template, context)


@login_required
def edit_profile(request):
    """View to edit the profile info"""
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'edit_profile.html'
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('profile'))
        else:
            messages.error(request,
                           ('Update failed. Please make sure '
                            'the information entered is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, template, context)


def view_past_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
    ))

    template = 'checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
