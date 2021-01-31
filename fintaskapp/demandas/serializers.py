from django.contrib.auth.models import User
from rest_framework import serializers
from demandas.models import Demanda


class DemandaAnuncianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class DemandaSerializer(serializers.ModelSerializer):
    anunciante = DemandaAnuncianteSerializer(read_only=True)

    class Meta:
        model = Demanda
        fields = ("anunciante", "id", "descricao", "endereco", "info_contato", "status", "data_criacao")
