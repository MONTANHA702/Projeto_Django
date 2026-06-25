from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import Autor, EixoTecnologia, Artigo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')

@admin.register(EixoTecnologia)
class EixoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_autor_nome', 'get_eixo_nome', 'data_publicacao')
    list_filter = ('id_fk_eixo', 'data_publicacao')
    search_fields = ('id_fk_autor__nome',)

    def get_autor_nome(self, obj):
        return obj.id_fk_autor.nome
    get_autor_nome.short_description = 'Autor'

    def get_eixo_nome(self, obj):
        return obj.id_fk_eixo.nome
    get_eixo_nome.short_description = 'Eixo Tecnológico'

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }