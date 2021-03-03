from django.shortcuts import render
from app.models import Veiculo, Oleo, Servico, TrocaDeOleo
from django.http import HttpResponse
from django.shortcuts import redirect
import sqlite3
# Create your views here.


def trocas_de_oleo(request):
    veiculos = list(Veiculo.objects.all().values())[:]
    oleos = list(Oleo.objects.all().values())[:]
    return render(request, 'trocas_de_oleo.html', {'veiculos': veiculos, 'oleos': oleos})


def nova_troca_de_oleo(request):
    veiculo = list(Veiculo.objects.filter(id=request.POST["id"]))[0]
    oleos = list(Oleo.objects.all().values())[:]
    trocas_de_oleo = list(TrocaDeOleo.objects.filter(
        veiculo_idveiculo=request.POST["id"]).values())[:]
    for troca in range(len(trocas_de_oleo)):
        oleo = list(Oleo.objects.filter(
            id=trocas_de_oleo[troca]["oleo_idoleo"]).values())[:]

        trocas_de_oleo[troca]["oleo"] = oleo[0]["nome"]
        trocas_de_oleo[troca]["proxkm"] = int(
            trocas_de_oleo[troca]["km_odometro"]) + int(oleo[0]["intervalo_de_troca_km"])

    return render(request, 'nova_troca_de_oleo.html', {'veiculo': veiculo, 'oleos': oleos, 'trocas': trocas_de_oleo})


def cadastrar_troca_de_oleo(request):
    data = request.POST["data"]
    valor = request.POST["valor"]
    valor = valor.replace(',', '.')

    veiculo_idveiculo = request.POST["veiculo_idveiculo"]
    oleo_idoleo = request.POST["oleo_idoleo"]
    km_odometro = request.POST["km_odometro"]
    troca_de_oleo = TrocaDeOleo(data=data, valor=valor, veiculo_idveiculo=veiculo_idveiculo,
                                oleo_idoleo=oleo_idoleo, km_odometro=km_odometro)
    troca_de_oleo.save()
    return redirect('/trocas_de_oleo')


def apagar_troca_de_oleo(request):
    troca = TrocaDeOleo.objects.filter(id=request.POST["trocaid"]).delete()
    return redirect('/trocas_de_oleo')
