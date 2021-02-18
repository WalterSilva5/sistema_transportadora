from django.urls import path

from .views.viewTelas import *
urlpatterns = [
    path('', index, name='index'),
    path('cadastros', cadastros, name='cadastros'),
    path('cadastros/cadastrar_veiculo', cadastrar_veiculo, name='cadastrar_veiculo'),
    path('cadastros/cadastrar_oleo', cadastrar_oleo, name='cadastrar_oleo'),
    path('cadastros/cadastrar_servico', cadastrar_servico, name='cadastrar_servico'),
]
