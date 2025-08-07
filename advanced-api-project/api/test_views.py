from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author  # import both

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create Author instances
        self.author1 = Author.objects.create(name="Author A")
        self.author2 = Author.objects.create(name="Author B")
        self.author3 = Author.objects.create(name="Author C")

        # Create Book instances with Author instances assigned
        self.book1 = Book.objects.create(title="Book One", author=self.author1, publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author=self.author2, publication_year=2021)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'Book Three',
            'author': self.author3.id,  # pass author ID, not string
            'publication_year': 2022
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Book Three')

    def test_get_books_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        data = {
            'title': 'Updated Title',
            'author': self.author1.id,  # use author ID here too
            'publication_year': self.book1.publication_year
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_year(self):
        url = reverse('book-list') + '?publication_year=2021'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)

    def test_authentication_required(self):
        client = APIClient()
        url = reverse('book-list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # or 401 if applicable