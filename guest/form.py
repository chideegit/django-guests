from django import forms
from .models import * 

class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'surname', 'email_id', 'phone_number', 'address', 'to_see']

class UpdateGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'surname', 'email_id', 'phone_number', 'address', 'to_see']