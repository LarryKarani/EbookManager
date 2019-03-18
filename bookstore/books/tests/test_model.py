from django.test import TestCase
from ..models import Book
from django.contrib.auth.models import User

# Create your tests here.

class BookModelTestcase(TestCase):
    """Contains the test tools for testing the book model"""

    def setUp(self):
        user = User.objects.create(username="tester")
        book = {
            'title': '1000 ways to die',
            'author': 'Jame King',
            'copies': 1
        }

        self.book = Book(title=book['title'], author=book['author'], copies=book['copies'], created_by=user)
        
    def test_model_can_create_a_bucketlist(self):
        """Test a model can add a book  to the database"""
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        
        self.assertNotEqual(old_count, new_count)
