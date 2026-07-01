from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from motorartigos.models import Autor, Artigo
from .forms import ArtigoForm



def artigos_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    artigos = Artigo.objects.filter(id_fk_autor=autor)
    return render(request, 'motorartigos/artigo_autor.html', {'autor': autor, 'artigos': artigos})

def artigo_detalhe(request):
    artigo_id = request.GET.get('id')
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'motorartigos/artigo_detalhe.html', {'artigo': artigo})

def index(request):
    autores = Autor.objects.all()

    # Para cada autor, busca o artigo mais recente dele.
    # A Meta do Artigo já ordena por -data_publicacao, então .first()
    # sempre traz o artigo mais novo (ou None, se o autor não tiver nenhum).
    for autor in autores:
        autor.ultimo_artigo = autor.artigo_set.first()

    return render(request, 'motorartigos/index.html', {'autores': autores})

def doc_gpt(request):
    return render(request, 'motorartigos/doc_gpt.html')
#ele precisa de uma rota que vamos colocar no urls.py

def doc_maritaca(request):
    return render(request, 'motorartigos/doc_maritaca.html')

def doc_minstral(request):
    return render(request, 'motorartigos/doc_minstral.html')

def doc_mysql(request):
    return render(request, 'motorartigos/doc_mysql.html')


def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)

            # Se o usuário NÃO enviou um arquivo novo, mas escolheu
            # uma foto existente na galeria, usamos ela.
            foto_existente = form.cleaned_data.get('foto_existente')
            if not request.FILES.get('foto') and foto_existente:
                artigo.foto = foto_existente

            artigo.save()
            return redirect('index')  # ajuste para sua rota real de destino

    else:
        form = ArtigoForm()

    return render(request, 'motorartigos/criar_artigo.html', {'form': form})
