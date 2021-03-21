from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create, name='create.post'),
    path('update/<int:post_id>', views.update, name='update.post'),
    path('delete/<int:post_id>', views.delete, name='delete.post'),
]