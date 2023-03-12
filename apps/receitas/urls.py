from django.urls import path
from apps.receitas.views import *

urlpatterns = [
    path('', index, name='index'),
    path('receita/<int:receita_id>', receita, name='receita'),
    path('busca', busca, name='busca'),
    path('cria_receita', cria_receita, name='cria_receita'),
    path('edita_receita/<int:receita_id>', edita_receita, name='edita_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita'),
    path('publica/<int:receita_id>', publica, name='publica'),
    path('apaga_receita/<int:receita_id>', apaga_receita, name='apaga_receita'),
]