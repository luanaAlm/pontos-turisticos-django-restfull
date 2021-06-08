from rest_framework.viewsets import ModelViewSet


from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
# filtro
from django_filters.rest_framework import DjangoFilterBackend


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [DjangoFilterBackend, ]
    search_fields = ['nome', 'descricao']
