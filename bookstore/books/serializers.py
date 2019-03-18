from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON formt."""
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        """Meta class to map serializer's field with the model fileds."""
        model = Book
        fields = ('id', 'title', 'author', 'copies', 'created_by')
        read_only_fields = ( 'date_added','date_modified')