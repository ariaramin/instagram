from django import forms
from .models import Post


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']