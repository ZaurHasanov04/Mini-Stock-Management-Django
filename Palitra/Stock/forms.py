from django import forms
from .models import *

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'phsyical_number', 'reserved_number', 'active_number']
        widgets={
            'product': forms.Select(attrs={'class':'select'}),
            'phsyical_number' : forms.NumberInput(attrs={'class':'phsyical_number'}),
            'reserved_number' : forms.NumberInput(attrs={'class':'reserved_number'}),
            'active_number' : forms.NumberInput(attrs={'class':'active_number'})
        }