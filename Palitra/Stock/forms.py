from django import forms
from .models import *

class StockForm(forms.ModelForm):
    # phsyical_number = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class':'phsyical_number'})
    # )
    class Meta:
        model = Stock
        fields = ['product', 'phsyical_number', 'reserved_number', 'active_number']
        widgets={
            'product': forms.Select(attrs={'class':'select'}),
        }