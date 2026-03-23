from django import forms
from .models import custmer

class CustmerForm(forms.ModelForm):
    class Meta:
        model=custmer
        fields=['name','email','phone','gst_number','address','is_active']