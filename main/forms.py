import re

from django import forms
from django.core.exceptions import ValidationError

from main.models import Product, Version


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        prohibited_names = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
            'casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap', 'free', 'fraud', 'police', 'radar'
        ]

        cleaned_data = self.cleaned_data['name']
        cleaned_data_lower = cleaned_data.lower()
        for word in prohibited_names:
            match = re.search(word, cleaned_data_lower)
            if match:
                raise ValidationError('Don\'t use prohibited words for the product\'s name!')

        return cleaned_data


class VersionForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
