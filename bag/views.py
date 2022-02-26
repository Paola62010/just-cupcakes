from django.shortcuts import render


def view_bag(request):
    """A view to render the bag page"""
    return render(request, 'bag.html')
