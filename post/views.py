from django.shortcuts import render, redirect
from .forms import PostForms
from .models import Post


# Create your views here.
def create(request):
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user.id
            f.save()
            return redirect('profile', request.user.id)
    return render(request, 'create.html')


def show(request):
    posts = Post.objects.all()
    # global posts
    # for following in request.user.profile.following.all():
    #     posts = Post.objects.filter(user_id=following)
    #     print(posts)
    return render(request, 'show.html', {'posts': posts})


def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.id)
    return render(request, 'update.html', {'post': post})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('profile', request.user.id)



