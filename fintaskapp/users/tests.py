import json
from django.urls import reverse
from rest_framework.test import APITestCase


class TestCreateUser(APITestCase):
    url = reverse("users:list")

    def test_invalid_password(self):
        user_data = {
            "username": "rafaelrizzatti",
            "email": "rafael.rizzatti@gmail.com",
            "password": "senha",
            "confirm_password": "senha_diferente"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_user_registration(self):
        user_data = {
            "username": "rafaelrizzatti",
            "email": "rafael.rizzatti@gmail.com",
            "password": "123",
            "confirm_password": "123"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)
        self.assertTrue("token" in json.loads(response.content))

    def test_unique_username_validation(self):
        user_data_1 = {
            "username": "rafaelrizzatti",
            "email": "rafael.rizzatti@gmail.com",
            "password": "123",
            "confirm_password": "123"
        }
        response = self.client.post(self.url, user_data_1)
        self.assertEqual(201, response.status_code)

        user_data_2 = {
            "username": "rafaelrizzatti",
            "email": "rafael.rizzatti@gmail.com",
            "password": "123",
            "confirm_password": "123"
        }
        response = self.client.post(self.url, user_data_2)
        self.assertEqual(400, response.status_code)