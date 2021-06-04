from django.db import models
from django.db.models.fields import TextField


class pontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome
