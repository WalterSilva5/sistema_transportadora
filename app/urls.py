from django.urls import path

from .views.views import *
urlpatterns = [
    path('', index, name='index'),
    path('relatorio', relatorio, name='relatorio'),

    path('cadastros', cadastros, name='cadastros'),
    path('cadastros/cadastrar_veiculo',
         cadastrar_veiculo, name='cadastrar_veiculo'),
    path('cadastros/cadastrar_oleo', cadastrar_oleo, name='cadastrar_oleo'),
    path('cadastros/apagar_veiculo',
         apagar_veiculo, name='apagar_veiculo'),
    path('cadastros/cadastrar_servico',
         cadastrar_servico, name='cadastrar_servico'),
    path('abastecimentos', abastecimentos, name='abastecimentos'),
    path('abastecimentos/por_veiculo', abastecimentos_por_veiculo,
         name="abastecimentos_por_veiculo"),
    path('abastecimentos/cadastrar_abastecimento',
         cadastrar_abastecimento, name="cadastrar_abastecimento"),
    path('abastecimentos/apagar_abastecimento', apagar_abastecimento, name="apagar_abastecimento"),
    path('servicos', servicos, name="servicos"),
    path('servicos/por_veiculo', servicos_por_veiculo,
         name="servicos_por_veiculo"),
    path('trocas_de_oleo', trocas_de_oleo, name="trocas_de_oleo"),
    path('trocas_de_oleo/nova_troca_de_oleo',
         nova_troca_de_oleo, name="nova_troca_de_oleo"),
    path('trocas_de_oleo/cadastrar_troca_de_oleo',
         cadastrar_troca_de_oleo, name="cadastrar_troca_de_oleo"),
    path('trocas_de_oleo/apagar_troca_de_oleo',
         apagar_troca_de_oleo, name="apagar_troca_de_oleo"),

]
