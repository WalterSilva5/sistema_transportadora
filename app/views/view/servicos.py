from django.shortcuts import render
from app.models import Veiculo, Oleo, Servico
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.


def servicos(request):
    veiculos = list(Veiculo.objects.all().values())[:]
    return render(request, 'servicos.html', {'veiculos': veiculos})


def servicos_por_veiculo(request):
    #veiculos = list(Veiculo.objects.all().values())[:]
    veiculo = list(Veiculo.objects.filter(placa=request.POST["placa"]))[0]
    servicos = list(Servico.objects.filter(
        veiculo_idveiculo=veiculo.id).order_by('data'))
    return render(request, 'servicos_por_veiculo.html', {'veiculo': veiculo, 'servicos': servicos})


def cadastrar_servico(request):
    descricao = request.POST["descricao"]
    data = request.POST["data"]
    valor = request.POST["valor"]
    valor = valor.replace(',', '.')

    veiculo_idveiculo = request.POST["id"]
    servico = Servico(descricao=descricao, data=data,
                      valor=valor, veiculo_idveiculo=veiculo_idveiculo)
    servico.save()
    return redirect('/')
