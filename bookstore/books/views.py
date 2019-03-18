from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import permissions
class CreateView(generics.ListCreateAPIView):
    """This class defines the add book behavior of the rest API"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        """ Save the post when adding a new book """
        serializer.save(created_by=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer