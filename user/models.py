from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account(User):
    bio = models.TextField(null=True)
    image = models.ImageField(upload_to='static/user/images', default='static/user/images/user.png', null=False)

    def __str__(self):
        return self.username
