from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email',
                  'phone', 'city', 'address_line1',
                  'address_line2', 'post_code', 'county',
                  'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove labels
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'city': 'City',
            'address_line1': 'Address line 1',
            'address_line2': 'Address line 2',
            'post_code': 'Post Code',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-inputs'
            self.fields[field].label = False
