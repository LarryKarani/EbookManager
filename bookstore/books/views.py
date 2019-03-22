from rest_framework import generics
from .serializers import BookSerializer, UserSerializer
from .models import Book
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view

class CreateView(generics.ListCreateAPIView):
    """This class defines the add book behavior of the rest API"""
    queryset = Book.objects.all()#query set that should be used in returning objects from this view
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        """ Save the post when adding a new book """
        serializer.save(created_by=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateUserView(generics.CreateAPIView):
    """Create user view"""
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()


#swagger documentation view
schema_view = get_swagger_view(title='BookManager API')
