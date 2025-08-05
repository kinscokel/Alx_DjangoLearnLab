from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Book

# Registering models so they show up in the admin site
admin.site.register(Author)
admin.site.register(Book)