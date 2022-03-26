from django import forms
from .models import jobApplication


class applicationForm(forms.ModelForm):
    class Meta:
        model = jobApplication
        exclude = ('job_posting',)
