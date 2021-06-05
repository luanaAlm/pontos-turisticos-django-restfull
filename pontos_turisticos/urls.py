from django import urls
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
# rest
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet

# rotas rest
router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
