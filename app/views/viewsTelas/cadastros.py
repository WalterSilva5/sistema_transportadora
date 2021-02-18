from django.shortcuts import render
from app.models import Veiculo, Oleo, Servico
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.


def cadastros(request):
    veiculos = list(Veiculo.objects.all().values())[:]
    oleos = list(Oleo.objects.all().values())[:]
    servicos = list(Servico.objects.all().values())[:]

    return render(request, 'cadastros.html', {'veiculos': veiculos, 'oleos': oleos, 'servicos':servicos})


def cadastrar_veiculo(request):
    placa = request.POST['placa']
    modelo = request.POST['modelo']
    ano = request.POST['ano']
    veiculo = Veiculo(placa=placa, modelo=modelo, ano=ano)
    veiculo.save()
    return redirect('/cadastros')

def cadastrar_oleo(request):
    nome = request.POST['nome']
    intervalo_de_troca_km = request.POST['intervalo_de_troca_km']
    oleo = Oleo(nome=nome, intervalo_de_troca_km=intervalo_de_troca_km)
    oleo.save()
    return redirect('/cadastros')

def cadastrar_servico(request):
    nome = request.POST['nome']
    servico = Servico(nome=nome)
    servico.save()
    return redirect('/cadastros')

def verificar_veiculo_cadastrado(placa):
    placa = Veiculo.objects.filter(placa=placa)
    return placa
