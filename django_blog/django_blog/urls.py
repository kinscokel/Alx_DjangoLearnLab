"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication
    path('register/', blog_views.register_view, name='register'),
    path('profile/', blog_views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  #  This includes your app's URLs
]


from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # List all blog posts
    path('posts/', PostListView.as_view(), name='post-list'),

    # Create a new post (authenticated users only)
    path('posts/new/', PostCreateView.as_view(), name='post-create'),

    # View a single post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Update a post (author only)
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete a post (author only)
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]