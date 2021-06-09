from django.db.models import query
from core.models import PontoTuristico

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import PontoTuristicoSerializer
from rest_framework.filters import SearchFilter
# autorização
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    # filtro
    filter_backends = [SearchFilter]
    # autorização
    #permission_classes = [DjangoModelPermissions]
    #authentication_classes = (TokenAuthentication,)

    search_fields = ['nome', 'descricao']
    lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(id=id)
        if nome:
            queryset.filter(nome__iexact=nome)
        if descricao:
            queryset.filter(descricao__iexact=descricao)
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # para alguns campos
    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request, pk=None):
        pass
