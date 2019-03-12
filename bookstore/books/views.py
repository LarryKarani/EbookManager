from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

class CreateView(generics.ListCreateAPIView):
    """This class defines the add book behavior of the rest API"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        """ Save the post when adding a new book """
        serializer.save()

