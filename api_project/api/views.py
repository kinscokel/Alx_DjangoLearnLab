from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions (CRUD) for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
# - Permission Classes:
# - IsAuthenticated ensures only logged-in users with valid tokens access endpoints.
# - Optionally use IsAdminOrReadOnly for admin-only edits.

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelViewSet(ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    permission_classes = [IsAuthenticated]  # Require token authentication

