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


def profile(request):
    posts = Post.objects.filter(user_id=request.user.id)
    posts_count = Post.objects.filter(user_id=request.user.id).count()
    return render(request, 'profile.html', {'posts': posts, 'posts_count': posts_count})




