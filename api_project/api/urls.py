# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList

router = DefaultRouter()
router.register(r'books', BookList, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
