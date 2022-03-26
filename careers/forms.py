from django import forms
from .models import jobApplication
from .widgets import CustomClearableFileInput


class applicationForm(forms.ModelForm):
    class Meta:
        model = jobApplication
        exclude = ('job_posting',)
