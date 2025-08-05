from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model): # Author models stores informations about book

    name = models.CharField(max_length=255) # Author's name

    def _str_(self):
        return self.name


# Book model represents a book and includes a foreign key to the Author model.

class Book(models.Model):
    tittle = models.CharField(max_length=225)    # Title of the book
    publication_year = models.IntegerField()     # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
 # related_name='books' allows reverse access to an author's books (e.g., author.books.all())

    def _str_(self):
        return self.tittle

from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)  
 
