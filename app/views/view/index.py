from django.shortcuts import render
from app.models import Veiculo, Abastecimento, TrocaDeOleo, Oleo, Servico
# Create your views here.
from django.http import HttpResponse
import json


def index(request):
    veiculos = list(Veiculo.objects.all().values())[:]
    registros = []

    for veiculo in veiculos:
        abastecimentos = list(Abastecimento.objects.filter(
            veiculo_idveiculo=veiculo["id"]).order_by('data').values())
        servicos = list(Servico.objects.filter(
            veiculo_idveiculo=veiculo["id"]).order_by('data').values())

        oleos = list(Oleo.objects.all().values())[:]
        trocas_de_oleo = list(TrocaDeOleo.objects.filter(
            veiculo_idveiculo=veiculo["id"]).values())[:]
        for troca in range(len(trocas_de_oleo)):
            oleo = list(Oleo.objects.filter(
                id=trocas_de_oleo[troca]["oleo_idoleo"]).values())[:]

            trocas_de_oleo[troca]["oleo"] = oleo[0]["nome"]
            trocas_de_oleo[troca]["proxkm"] = int(
                trocas_de_oleo[troca]["km_odometro"]) + int(oleo[0]["intervalo_de_troca_km"])

        registros.append({"veiculo": veiculo, "abastecimentos": abastecimentos,
                          "servicos": servicos, "trocas_de_oleo": trocas_de_oleo})

    return render(request, 'index.html', {'registros': registros})


def relatorio(request):
    veiculo = list(Veiculo.objects.filter(id=request.POST["id"]).values())[0]
    abastecimentos = list(Abastecimento.objects.filter(
        veiculo_idveiculo=request.POST["id"]).order_by('data').values())
    servicos = list(Servico.objects.filter(
        veiculo_idveiculo=request.POST["id"]).order_by('data').values())

    oleos = list(Oleo.objects.all().values())[:]
    trocas_de_oleo = list(TrocaDeOleo.objects.filter(
        veiculo_idveiculo=request.POST["id"]).values())[:]
    for troca in range(len(trocas_de_oleo)):
        oleo = list(Oleo.objects.filter(
            id=trocas_de_oleo[troca]["oleo_idoleo"]).values())[:]

        trocas_de_oleo[troca]["oleo"] = oleo[0]["nome"]
        trocas_de_oleo[troca]["proxkm"] = int(
            trocas_de_oleo[troca]["km_odometro"]) + int(oleo[0]["intervalo_de_troca_km"])

    registro = {"veiculo": veiculo, "abastecimentos": abastecimentos,
                "servicos": servicos, "trocas_de_oleo": trocas_de_oleo}

    return render(request, 'relatorio.html', {"registro": registro})
