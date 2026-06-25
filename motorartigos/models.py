from django.db import models
from tinymce.models import HTMLField
# Create your models here.
# Aqui vou criar minhas classes de entidade (banco de dados)

class Autor(models.Model):
    
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'autor' #retira o nome gigante

class EixoTecnologia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'eixo' #retira o nome gigante

class Artigo(models.Model):         
    texto = HTMLField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
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
        return f"Artigo {self.id} - {self.data_publicacao}"

    class Meta:
        db_table = 'artigo'