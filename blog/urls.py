from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='post'),
    path('posts/<slug:slug>', views.post_details, name='post-details'),
]
