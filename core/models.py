from __future__ import unicode_literals
from django.db import models
#from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

TIPOS_DE_ANIMAL = (
	('CACHORRO', 'Cachorro'),
	('AVES', 'Passarinho'),
	('GATO', 'Gato'),
	)

SEXO = (
	('M', 'Macho'),
	('F', 'Femea')
	)

ESTADOS = (
	('PB', 'Paraiba'),
	('PE', 'Pernambuco'),
	)

SERVICOS = (
	('BT', 'Banho e Tosa'),
	('V', 'Vacinacao'),
	('C', 'Castracao')
	)

class Animal(models.Model):
	especie = models.CharField(max_length=255, choices=TIPOS_DE_ANIMAL)
	nome = models.CharField(max_length=255)
	idade = models.IntegerField()
	sexo = models.CharField(max_length=5,choices=SEXO)
	foto = models.ImageField(null=True, blank=True)
	dono = models.ForeignKey('Cliente', null=True, related_name='animais')

	def __unicode__(self):
		return self.nome

class Cliente(models.Model):
	nome = models.CharField(max_length=255)
	telefone = models.CharField(max_length=255)
	cpf = models.CharField(max_length=11)
	endereco = models.ForeignKey('Endereco', null=True, related_name='clientes')
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='cliente')

	def __unicode__(self):
		return self.nome

class Endereco(models.Model):
	estado = models.CharField(max_length=255, choices=ESTADOS)
	cidade = models.CharField(max_length=255)
	bairro = models.CharField(max_length=255)
	rua = models.CharField(max_length=255)
	numero = models.CharField(max_length=255)

	def __unicode__(self):
		return self.rua + ', ' + self.bairro + ', ' + self.cidade

class Servicos(models.Model):
	servico = models.CharField(max_length=255, choices=SERVICOS)
