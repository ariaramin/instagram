from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from post.models import Post

# Create your views here.


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'registration/register.html', {'form': form})


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.filter(user_id=user_id)
    return render(request, 'profile.html', {'posts': posts, 'user': user})


