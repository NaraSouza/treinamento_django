# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170214_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapa'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceara'), ('DF', 'Distrito Federal'), ('ES', 'Espirito Santo'), ('GO', 'Goias'), ('MA', 'Maranhao'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Para'), ('PB', 'Paraiba'), ('PR', 'Parana'), ('PE', 'Pernambuco'), ('PI', 'Piaui'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondonia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'Sao Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]