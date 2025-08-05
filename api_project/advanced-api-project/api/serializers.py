from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer handles the serialization of Book model instances.
class BookSerializers(serializer.ModelSerializer):
    class meta:
        model=Book
        fields = '_all_'  # Serialize all fields

    # Custom validation to ensure publication_year is not in the future.
    def validate_publication_year = (self, value):
        current_year = datetime.now().current_year
        if value > current_year:
            raise serialization.VliadtionError("publication can not be in the future.")
            return value


# AuthorSerializer handles serialization of Author instances,
# and includes a nested BookSerializer for related books.

class AuthorSerializer(serializer.ModelSerializer):
     books = BookSerializer(many=True, read_only=True)

       class Meta:
        model = Author
        fields = ['name', 'books']

    
