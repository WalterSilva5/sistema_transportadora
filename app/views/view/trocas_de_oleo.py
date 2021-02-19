from django.shortcuts import render
from app.models import Veiculo, Oleo, Servico
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.


def trocas_de_oleo(request):
    veiculos = list(Veiculo.objects.all().values())[:]
    oleos = list(Oleo.objects.all().values())[:]
    return render(request, 'trocas_de_oleo.html', {'veiculos': veiculos, 'oleos': oleos})


def nova_troca_de_oleo(request):
    oleos = list(Oleo.objects.all().values())[:]
    return render(request, 'nova_troca_de_oleo.html', {'veiculos': veiculos, 'oleos': oleos})
