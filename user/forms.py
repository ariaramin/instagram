from django import forms
from .models import Account


class AccountForms(forms.ModelForm):
    class Meta:

        model = Account
        fields = ['image', 'bio']
