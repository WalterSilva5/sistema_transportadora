# Generated by Django 3.1.6 on 2021-02-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_oleo_servico_servicoefetuado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abastecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='data')),
                ('valor', models.FloatField(verbose_name='valor')),
                ('veiculo_idveiculo', models.IntegerField(verbose_name='veiculo_idveiculo')),
            ],
        ),
    ]