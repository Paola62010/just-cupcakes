from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import jobApplication, jobPosting
from .forms import applicationForm


def job_postings(request):
    postings = jobPosting.objects.all()

    template = 'job_postings.html'
    context = {
        'postings': postings
    }

    return render(request, template, context)


def job_application(request, posting_id):
    posting = get_object_or_404(jobPosting, id=posting_id)

    if request.method == 'POST':
        form = applicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.job_posting = posting
            application = form.save(commit=False)
            application.posting = posting
            application.save()
            messages.success(request, 'Application sent successfully.')
            return redirect(reverse('job_postings'))
        else:
            messages.error(request,
                           ('Sorry, your application could not be sent. '
                            'Make sure the entered information is '
                            'valid.'))
    else:
        form = applicationForm()

    template = 'application.html'
    context = {
        'form': form,
        'posting': posting
    }

    return render(request, template, context)
