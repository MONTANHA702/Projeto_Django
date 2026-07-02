from django.db import models
from tinymce.models import HTMLField
from django.templatetags.static import static

# Create your models here.
# Aqui vou criar minhas classes de entidade (banco de dados)

class Autor(models.Model):

    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'autor'  # retira o nome gigante
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class EixoTecnologia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'eixo'  # retira o nome gigante


class Artigo(models.Model):

    TAG_NIVEL = [
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    ]

    titulo = models.CharField(max_length=200, default='Sem título')
    texto = HTMLField()
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    tag_nivel = models.CharField(max_length=1, choices=TAG_NIVEL, default='B')
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    


    @property
    def image_url(self):
        if self.foto:
            return self.foto.url
        return static('img/default_card.png')

    id_fk_eixo = models.ForeignKey(
        EixoTecnologia,
        on_delete=models.CASCADE,
        db_column='id_fk_eixo'
    )
    id_fk_autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        db_column='id_fk_autor'
    )

    def __str__(self):
        return f"Artigo {self.id} – {self.id_fk_autor}"

    class Meta:
        db_table = 'artigo'
        ordering = ['-data_publicacao']