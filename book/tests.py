from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APITestCase
from account.tests import TokenFactory
from book.models import Book, Author, Genre
import factory


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker('name')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    name = factory.Faker('name')
    description = factory.Faker('text')
    slug = factory.Faker('name')
    genre = factory.SubFactory(GenreFactory)
    author = factory.SubFactory(AuthorFactory)


class TestProduct(APITestCase):

    def test_list(self):
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get("/api/book/")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_retrieve(self):
        book = BookFactory()
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(f"/api/book/{book.id}/")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_favorite(self):
        book = BookFactory()
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(f"/api/book-favorite/{book.id}/")
        self.assertEqual(response.status_code, HTTP_200_OK)
