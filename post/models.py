from django.contrib.auth.models import User
from user.models import Profile
from django.db import models


# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='static/post/images')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
