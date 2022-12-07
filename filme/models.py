from django.db import models
from django.utils import timezone
# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programção"),
    ("APRESENTRACAO", "Apresentação"),
    ("OUTROS", "Outros")
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_lenght=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)


# criar os episodios

# criar o usuário