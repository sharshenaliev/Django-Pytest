from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
import factory


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = 'test_user@mail.com'
    password = factory.PostGenerationMethodCall('set_password', 'test_password')


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token

    user = factory.SubFactory(UserFactory)


class TestUser(APITestCase):

    def test_register(self):
        user = UserFactory.build()
        data = {"email": user.email, "password": user.password, "password2": user.password}
        response = self.client.post("/auth/register/", data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_login(self):
        user = UserFactory()
        data = {"email": user.email, "password": 'test_password'}
        response = self.client.post("/auth/login/", data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_logout(self):
        token = TokenFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete('/auth/logout/')
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
