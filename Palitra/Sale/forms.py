from django import forms
from .models import *
from Stock.models import *

class SaleForm(forms.ModelForm):
    reserved_date = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y',attrs={'class':'datetimepicker', 'placeholder':'Tarixi sec'},),
        input_formats=['%d-%m-%Y'])
    class Meta:
        model = Sale
        fields = ['stock','contract_type', 'contract_code', 'reserved_status', 'reserved_date','sale_number']
        widgets={
            'stock': forms.Select(attrs={'class':'select'}),
            'contract_type': forms.Select(attrs={'class':'select'}),     
            
        }
  