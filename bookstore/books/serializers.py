from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON formt."""
    class Meta:
        """Meta class to map serializer's field with the model fileds."""
        model = Book
        fields = ('id', 'title', 'author', 'copies', 'date_added','date_modified')