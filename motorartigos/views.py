from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from motorartigos.models import Autor, Artigo





autores = Autor.objects.all()
def artigos_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    artigos = Artigo.objects.filter(id_fk_autor=autor)
    return render(request, 'motorartigos/artigo_autor.html', {'autor': autor, 'artigos': artigos})
 
def artigo_detalhe(request):
    artigo_id = request.GET.get('id')
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'motorartigos/artigo_detalhe.html', {'artigo': artigo})

def index(request):
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
