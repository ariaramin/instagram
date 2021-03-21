from django.shortcuts import render, redirect
from .forms import PostForms


# Create your views here.
def create(request):
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'create.html')