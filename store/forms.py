from django import forms
from .widgets import CustomClearableFileInput
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'category',
            'name',
            'sku',
            'description',
            'price',
            'image',
            'popular'
        )

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)
