from django import forms
from .models import products

class productform(forms.ModelForm):
    class Meta:
        model = products
        fields = ['name','product_type','stock_unit','price','stock','is_active']