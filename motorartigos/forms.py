import os
from django import forms
from django.conf import settings
from .models import Artigo


def listar_fotos_existentes():
    """Varre a pasta media/fotos (e subpastas de data) e retorna
    os caminhos relativos das imagens já existentes."""
    pasta_fotos = os.path.join(settings.MEDIA_ROOT, 'fotos')
    fotos = []

    if os.path.exists(pasta_fotos):
        for raiz, _, arquivos in os.walk(pasta_fotos):
            for nome in arquivos:
                if nome.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                    caminho_completo = os.path.join(raiz, nome)
                    caminho_relativo = os.path.relpath(caminho_completo, settings.MEDIA_ROOT)
                    fotos.append(caminho_relativo.replace('\\', '/'))  # normaliza pro padrão de URL

    return sorted(fotos, reverse=True)  # mais recentes primeiro


class ArtigoForm(forms.ModelForm):
    foto_existente = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        label='Ou escolha uma foto já existente em media/fotos',
    )

    class Meta:
        model = Artigo
        fields = [
            'titulo',
            'texto',
            'foto',
            'tag_nivel',
            'publicada',
            'id_fk_eixo',
            'id_fk_autor',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input-titulo', 'placeholder': 'Título do artigo'}),
            'tag_nivel': forms.Select(attrs={'class': 'input-select'}),
            'id_fk_eixo': forms.Select(attrs={'class': 'input-select'}),
            'id_fk_autor': forms.Select(attrs={'class': 'input-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto_existente'].choices = [
            (caminho, caminho) for caminho in listar_fotos_existentes()
        ]
        self.fields['foto'].required = False  # upload novo vira opcional
