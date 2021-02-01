import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from demandas.models import Demanda


class ListarDemandas(APITestCase):
    url = reverse("demandas:list")

    def setUp(self):
        self.username = "rafael"
        self.email = "rafael.rizzatti@gmail.com"
        self.password = "123"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_demanda(self):
        response = self.client.post(self.url, {"descricao": "Arma Especial a Laser", "endereco": "Rua Estrela Negra,"
                                               + "n 555", "info_contato": "(47) 99797-9797"})
        self.assertEqual(201, response.status_code)

    def test_user_demandas(self):
        Demanda.objects.create(anunciante=self.user, descricao="Arma Especial a Laser",
                               endereco="Rua Estrela Negra, n 555",
                               info_contato="(47) 99797-9797")
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Demanda.objects.count())