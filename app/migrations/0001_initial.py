# Generated by Django 3.1.6 on 2021-02-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=100, unique=True, verbose_name='placa')),
                ('modelo', models.CharField(max_length=100, verbose_name='modelo')),
                ('ano', models.IntegerField(verbose_name='ano')),
            ],
        ),
    ]
