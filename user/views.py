from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from .forms import AccountForms

# Create your views here.


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


