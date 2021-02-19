from django.shortcuts import render
from app.models import Veiculo, Oleo, Servico, Abastecimento
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.


def abastecimentos(request):
    veiculos = list(Veiculo.objects.all().values())[:]
    return render(request, 'abastecimentos.html', {'veiculos': veiculos})

def abastecimentos_por_veiculo(request):
    #veiculos = list(Veiculo.objects.all().values())[:]
    veiculo = list(Veiculo.objects.filter(placa=request.POST["placa"]))[0]
    abastecimentos = list(Abastecimento.objects.filter(veiculo_idveiculo=veiculo.id).order_by('data'))
    return render(request, 'abastecimentos_por_veiculo.html', {'veiculo': veiculo, 'abastecimentos': abastecimentos})

def cadastrar_abastecimento(request):
    data = request.POST["data"]
    valor = request.POST["valor"]
    veiculo_idveiculo = request.POST["id"]
    abastecimento = Abastecimento(data=data, valor=valor, veiculo_idveiculo=veiculo_idveiculo)
    abastecimento.save()
    return redirect('/')