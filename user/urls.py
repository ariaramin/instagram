from django.conf.urls.static import static
from django.urls import path, include
from instagram import settings
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('edit/<int:user_id>', views.edit, name='edit'),
    path('profile/', views.profile, name='profile'),
]

