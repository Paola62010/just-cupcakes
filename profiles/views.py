from django.shortcuts import render


def view_profile(request):
    """Displays the user's profile"""
    template = 'profile.html'
    context = {}

    return render(request, template, context)
