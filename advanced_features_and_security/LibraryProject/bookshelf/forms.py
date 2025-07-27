from django import forms
from .models import Book  # Make sure your Book model exists

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']