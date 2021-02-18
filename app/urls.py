from django.urls import path

from .views.views import *
urlpatterns = [
    path('', index, name='index'),
    path('cadastros', cadastros, name='cadastros'),
    path('cadastros/cadastrar_veiculo',
         cadastrar_veiculo, name='cadastrar_veiculo'),
    path('cadastros/cadastrar_oleo', cadastrar_oleo, name='cadastrar_oleo'),
    path('cadastros/cadastrar_servico',
         cadastrar_servico, name='cadastrar_servico'),
    path('abastecimentos', abastecimentos, name='abastecimentos'),
    path('abastecimentos/por_veiculo', abastecimentos_por_veiculo, name="abastecimentos_por_veiculo"),
    path('abastecimentos/cadastrar_abastecimento', cadastrar_abastecimento, name="cadastrar_abastecimento"),

]
