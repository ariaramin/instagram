from django.db import models


# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='static/post/images')
    # like = models.IntegerField(max_length=100)
    description = models.TextField()
    # user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)