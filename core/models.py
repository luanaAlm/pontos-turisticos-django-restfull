from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(
        Endereco, on_delete=CASCADE, blank=True, null=True)
    foto = models.ImageField(
        upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
