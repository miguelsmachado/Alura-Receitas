from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Receitas(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    rendimento = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    foto_receita = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    data = models.DateTimeField(default=datetime.now(), blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_receita
