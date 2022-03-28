from django.shortcuts import render


def home(request):
    """A view to render the home page"""
    return render(request, 'index.html')


def about(request):
    """A view to render the about page"""
    return render(request, 'about.html')
