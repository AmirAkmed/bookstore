from django.test import TestCase
from django.urls import reverse
from .models import Author, Book

# Create your tests here.

class AuthorTests(TestCase):
    
    def setUp(self):
        self.author = Author.objects.create(name='John Doe', biography='An unknown author')

    def test_author_list_view(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertTemplateUsed(response, 'books/author_list.html')

    def test_author_detail_view(self):
        response = self.client.get(reverse('author_detail', args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertTemplateUsed(response, 'books/author_detail.html')

    def test_author_create_view(self):
        response = self.client.post(reverse('author_create'), {
            'name': 'Jane Doe',
            'biography': 'Another unknown author'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Author.objects.last().name, 'Jane Doe')

    def test_author_update_view(self):
        response = self.client.post(reverse('author_update', args=[self.author.id]), {
            'name': 'John Smith',
            'biography': 'An updated biography'
        })
        self.assertEqual(response.status_code, 302)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, 'John Smith')

    def test_author_delete_view(self):
        response = self.client.post(reverse('author_delete', args=[self.author.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Author.objects.count(), 0)

class BookTests(TestCase):
    
    def setUp(self):
        self.author = Author.objects.create(name='John Doe', biography='An unknown author')
        self.book = Book.objects.create(title='Sample Book', publication_date='2023-01-01', author=self.author)

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Book')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Book')
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_book_create_view(self):
        response = self.client.post(reverse('book_create'), {
            'title': 'Another Book',
            'publication_date': '2024-01-01',
            'author': self.author.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().title, 'Another Book')

    def test_book_update_view(self):
        response = self.client.post(reverse('book_update', args=[self.book.id]), {
            'title': 'Updated Book',
            'publication_date': '2023-01-01',
            'author': self.author.id
        })
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_book_delete_view(self):
        response = self.client.post(reverse('book_delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 0)
