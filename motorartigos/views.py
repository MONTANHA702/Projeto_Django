from django.shortcuts import render
from django.http import HttpResponse
from motorartigos.models import Autor




'''  

autores = {
    1:{'nome':'André Roglem', 'biografia': 'Desenvolvedor Django', 'email':'fernando@gmail.com'},
    2:{'nome':'Fernando Oliveira', 'biografia': 'Desenvolvedor Django', 'email':'oliveira@gmail.com'},
    3:{'nome':'Cristina Oliveira', 'biografia': 'Desenvolvedor SQL', 'email':'cristina@gmail.com'}
}
'''

autores = Autor.objects.all()
 
def index(request):
    return render(request, 'motorartigos/index.html', {'autores': autores})

def artigo(request):
    return render(request, 'motorartigos/artigo.html')
#ele precisa de uma rota que vamos colocar no urls.py

def doc_maritaca(request):
    return render(request, 'motorartigos/doc_maritaca.html')

def doc_minstral(request):
    return render(request, 'motorartigos/doc_minstral.html')

def doc_mysql(request):
    return render(request, 'motorartigos/doc_mysql.html')
