from django.test import TestCase
from ..models import Book
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and dummy test data"""
        self.client = APIClient()
        self.valid_payload = {
            "title": "Boss baby",
            'author': "Adrew Kings",
            'copies': 23
        }
        self.response = self.client.post(
            reverse('create'),
            self.valid_payload,
            format="json")

    def test_api_can_add_a_book(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


