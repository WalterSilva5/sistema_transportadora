from django.db import models

# Create your models here.

class Veiculo(models.Model):
    placa = models.CharField('placa', max_length=100, null=False, blank=False, unique=True)
    modelo = models.CharField('modelo', max_length=100)
    ano = models.IntegerField('ano')

class Oleo(models.Model):
    nome = models.CharField('nome', max_length=100, null=False, blank=False, unique=True)
    intervalo_de_troca_km = models.IntegerField('intervalo_de_troca_km')

class Servico(models.Model):
    nome = models.CharField('placa', max_length=100, null=False, blank=False, unique=True)

class ServicoEfetuado(models.Model):
    data = models.DateTimeField('data')
    valor = models.FloatField('valor')
    servico_idservico = models.IntegerField('servico_idservico')
    veiculo_idveiculo = models.IntegerField('veiculo_idveiculo')
    
class Abastecimento(models.Model):
    data = models.DateTimeField('data')
    valor = models.FloatField('valor')
    veiculo_idveiculo = models.IntegerField('veiculo_idveiculo')
