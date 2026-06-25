
from django.urls import path
from motorartigos.views import index, artigo, doc_maritaca, doc_minstral, doc_mysql

#boa prática
#cada app se vira com suas rotas

urlpatterns = [
    path('', index),
    path('artigo/', artigo, name='artigo'), #rota para o views.py
    #name='artigo' é uma apelido para ser chamado no index.html
    path('doc_maritaca/', doc_maritaca, name='doc_maritaca'),
    path('doc_minstral/', doc_minstral, name='doc_minstral'),
    path('doc_mysql/', doc_mysql, name='doc_mysql'),
   
]

