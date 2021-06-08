from re import M
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto')
