from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    LikeView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home' ),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail' ),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update' ),
    path('post/new/', PostCreateView.as_view(), name = 'post-create' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete' ),
    path('about', views.about, name = 'blog-about'),
    path('announcement', views.announcement, name = 'blog-announcement'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    

]