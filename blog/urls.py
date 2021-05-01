from django.urls import path, include
from . import views

from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView,PostDeleteView, UserPostListView)

urlpatterns = [
    # path('', views.home, name='blog-home'),
    #use Class based view
    #path('',PostListView.as_view(template_name='blog/blog_home.html', context_object_name='posts'),name='blog-home'),
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('about/', views.about, name="blog-about"),
    
]
