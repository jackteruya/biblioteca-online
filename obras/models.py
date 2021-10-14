from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=250)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Obras(models.Model):
    titulo = models.CharField(max_length=250)
    editora = models.CharField(max_length=250)
    foto = models.URLField()
    autores = models.ManyToManyField(Autor)
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['data_criacao']

    def __str__(self):
        return self.titulo
