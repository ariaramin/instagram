from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('edit/<int:user_id>', views.edit, name='edit'),
    path('profile/<int:user_id>', views.profile, name='profile'),
]

