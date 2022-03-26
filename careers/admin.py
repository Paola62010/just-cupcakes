from django.contrib import admin
from .models import jobApplication, jobCategory, jobPosting


@admin.register(jobCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(jobPosting)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on',)
    list_filter = ('created_on', 'updated_on',)
    search_fields = ('title',)


@admin.register(jobApplication)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('job_posting', 'name', 'last_name', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('name', 'last_name',)
