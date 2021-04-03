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
            f = form.save()
            Profile.objects.create(user_id=f.id)
            return redirect('login')
    return render(request, 'registration/register.html', {'form': form})


def edit(request, user_id):
    user = Profile.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = ProfileForms(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id)
    return render(request, 'profile.html')


def profile(request, user_id):
    context = {
        'user': Profile.objects.get(user_id=user_id),
        'posts': Post.objects.filter(user_id=user_id),
    }
    return render(request, 'profile.html', context)


def follow(request, user_id):
    user = Profile.objects.get(user_id=request.user.id)
    user.following.add(user_id)
    # print(user.following.get(username='ariaramin'))
    user.save()
    return redirect('profile', user_id)


def unfollow(request, user_id):
    user = Profile.objects.get(user_id=request.user.id)
    user.following.remove(user_id)
    return redirect('profile', user_id)