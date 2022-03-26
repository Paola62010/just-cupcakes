from django.urls import path
from . import views

urlpatterns = [
    path('job_postings', views.job_postings, name='job_postings'),
]
