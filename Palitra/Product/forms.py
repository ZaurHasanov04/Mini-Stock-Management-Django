from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['brand', 'product_article', 'product_model']
        widgets = {
            'brand': forms.Select(attrs={'class':'select'}),
        }