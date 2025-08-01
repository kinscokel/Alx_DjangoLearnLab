# api/urls.py

from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # Existing ListAPIView route (if needed)
    path('books/', BookList.as_view(), name='book-list'),

    # Automatically generated CRUD routes for BookViewSet
    path('', include(router.urls)),
]
