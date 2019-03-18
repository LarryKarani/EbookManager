
from django.test import TestCase
from ..models import Book
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and dummy test data"""
        user = User.objects.create(username='tester')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        

        self.valid_payload = {
            "title": "Boss baby",
            'author': "Adrew Kings",
            'copies': 23,
            'created_by': user.id
        }

        
        
        self.response = self.client.post(
            reverse('create'),
            self.valid_payload,
            format="json")
        

    def test_api_can_add_a_book(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_book(self):
        """Test the api can get a given book."""
        book = Book.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': book.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, book)

    def test_api_can_update_book(self):
        """Test the api can update a given book."""
        book_update= {
            "title": "KingsMan Secret service",
            'author': "Adrew Kings",
            'copies': 2
        }
        book = Book.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': book.id}),
            book_update, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_book(self):
        """Test the api can delete a book."""
        book = Book.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': book.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    