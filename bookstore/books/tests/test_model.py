from django.test import TestCase
from ..models Book

# Create your tests here.

class BookModelTestcase(TestCase):
    """Contains the test tools for testing the book model"""

    def setUp(self):
        book = {
            'title': '1000 ways to die',
            'author': 'Jame King',
            'copies': 1
        }

        self.book = Book(title=book['title'], author=book['author'], copies=book['copies'])
    
    def test_model_can_create_a_bucketlist(self):
        """Test a model can add a book  to the database"""
        old_count = Books.objects.count()
        self.bucketlist.save()
        new_count = Books.objects.count()

        self.assertNotEqual(old_count, new_count)
