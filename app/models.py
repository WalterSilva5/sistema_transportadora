from django.db import models
from django.utils.timezone import now
# Create your models here.


class Veiculo(models.Model):
    placa = models.CharField('placa', max_length=100,
                             null=False, blank=False, unique=True)
    modelo = models.CharField('modelo', max_length=100)
    ano = models.IntegerField('ano')


class Oleo(models.Model):
    nome = models.CharField('nome', max_length=100,
                            null=False, blank=False, unique=True)
    intervalo_de_troca_km = models.IntegerField('intervalo_de_troca_km')


class Servico(models.Model):
    descricao = models.CharField('descricao', max_length=250)
    data = models.DateTimeField('data', default=now, blank=True)
    valor = models.FloatField('valor', default=0)
    veiculo_idveiculo = models.IntegerField('veiculo_idveiculo')


class Abastecimento(models.Model):
    data = models.DateTimeField('data')
    valor = models.FloatField('valor', blank=True)
    veiculo_idveiculo = models.IntegerField('veiculo_idveiculo')


class TrocaDeOleo(models.Model):
    data = models.DateTimeField('data')
    valor = models.FloatField('valor', blank=True)
    oleo_idoleo = models.IntegerField('oleo_idoleo')
    veiculo_idveiculo = models.IntegerField('veiculo_idveiculo')
    km_odometro = models.IntegerField('km_odometro')
