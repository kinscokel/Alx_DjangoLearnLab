from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

]

# relationship_app/urls.py
rom django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]