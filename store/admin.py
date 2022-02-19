from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.site_header = 'Just Cupcakes Administration'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_on', 'updated_on',)
    list_filter = ('created_on', 'updated_on',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'sku', 'price',
                    'created_on', 'updated_on',)
    list_filter = ('created_on', 'updated_on',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'created_by__username',)
    exclude = ('created_by',)
