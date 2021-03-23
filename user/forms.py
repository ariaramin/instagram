from django import forms
from .models import Profile


class ProfileForms(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ['bio', 'image']
