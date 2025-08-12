# from django.urls import path
#from . import views

# urlpatterns = [
    # Example route, add yours here
 #   path('', views.home, name='home'),  # Assuming you have a `home` view




# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
  #  path('', views.home, name='home'),

    # Authentication URLs
  #  path('register/', views.register_view, name='register'),
    #path('profile/', views.profile_view, name='profile'),

    # Built-in auth views for login/logout with custom templates
 #   path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
  #  path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),



# blog/urls.py
# from django.urls import path
# from .views import (
  #  PostListView, PostDetailView, PostCreateView,
  #  PostUpdateView, PostDeleteView


# urlpatterns = [
  #  path('posts/', PostListView.as_view(), name='post-list'),
  #  path('posts/new/', PostCreateView.as_view(), name='post-create'),
  #  path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  #  path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
  #  path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
  # ]

from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/', views.profile_view, name='profile'),
]


from django.urls import path
from . import views

urlpatterns = [
    # Other paths
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add_comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]


from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    #  Comment URLs
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]