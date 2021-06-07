from django import urls
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
# rest
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from enderecos.api.viewsets import EnderecoViewSet


# rotas rest
router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet)
router.register(r'enderecos', EnderecoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
