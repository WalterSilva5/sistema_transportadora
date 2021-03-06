# Generated by Django 3.1.6 on 2021-02-19 13:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_abastecimento'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServicoEfetuado',
        ),
        migrations.AddField(
            model_name='servico',
            name='data',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='data'),
        ),
        migrations.AddField(
            model_name='servico',
            name='valor',
            field=models.FloatField(default=0, verbose_name='valor'),
        ),
        migrations.AddField(
            model_name='servico',
            name='veiculo_idveiculo',
            field=models.IntegerField(default=1, verbose_name='veiculo_idveiculo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='valor',
            field=models.FloatField(blank=True, verbose_name='valor'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='nome',
            field=models.CharField(max_length=250, unique=True, verbose_name='placa'),
        ),
    ]
