from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import ProfileForms
from post.models import Post


# Create your views here.


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'registration/register.html', {'form': form})


def edit(request, user_id):
    user = Profile.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = ProfileForms(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'profile.html')


def profile(request):
    context = {
        'user': Profile.objects.get(user_id=request.user.id),
        'posts': Post.objects.filter(user_id=request.user.id),
        'posts_count': Post.objects.filter(user_id=request.user.id).count(),
    }
    return render(request, 'profile.html', context)
