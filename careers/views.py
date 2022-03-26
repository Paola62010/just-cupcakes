from django.shortcuts import render
from .models import jobApplication, jobCategory, jobPosting


def job_postings(request):
    postings = jobPosting.objects.all()

    template = 'job_postings.html'
    context = {
        'postings': postings
    }

    return render(request, template, context)
