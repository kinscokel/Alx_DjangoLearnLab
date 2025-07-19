from django.shortcuts import render

# Create your views here.
# Function based view
from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})



# Class based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'