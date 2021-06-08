from core.models import PontoTuristico

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})

    def create(self, request, *args, **kwargs):
        return Response({'Hello': request.data['nome']})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    # para alguns campos
    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request, pk=None):
        pass
