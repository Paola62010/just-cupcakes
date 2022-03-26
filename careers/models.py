from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField


class jobCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class jobPosting(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(jobCategory,
                                 on_delete=models.CASCADE)
    description = models.TextField()
    experience = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class jobApplication(models.Model):
    job_posting = models.ForeignKey(jobPosting, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=250, null=True)
    message = models.TextField(blank=True, null=True)
    resume = CloudinaryField(blank=False,
                             resource_type="auto")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Application {self.id} for {self.job_posting.title}'
