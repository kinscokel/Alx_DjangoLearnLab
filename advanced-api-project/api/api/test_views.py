from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.book = Book.objects.create(
            title="Test Book",
            author="Author A",
            published_date="2023-01-01",
            isbn="1234567890123"
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.list_url = reverse('book-list')

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Author B",
            "published_date": "2024-01-01",
            "isbn": "9876543210123"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_book(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    def test_update_book(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_unauthenticated_user_cannot_create_book(self):
        self.client.logout()
        data = {
            "title": "Unauthorized",
            "author": "Author C",
            "published_date": "2022-05-05",
            "isbn": "5555555555555"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {'author': 'Author A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for book in response.data:
            self.assertEqual(book['author'], 'Author A')

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for book in response.data:
            self.assertIn('Test', book['title'])

    def test_order_books_by_published_date(self):
        Book.objects.create(
            title="Old Book",
            author="Author D",
            published_date="2020-01-01",
            isbn="4444444444444"
        )
        response = self.client.get(self.list_url, {'ordering': 'published_date'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dates = [book['published_date'] for book in response.data]
        self.assertEqual(dates, sorted(dates))
