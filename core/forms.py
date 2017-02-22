#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Endereco, Cliente, Animal, ESTADOS, SERVICOS

class UsuarioForm(forms.Form):
	email = forms.EmailField(max_length=255)
	senha = forms.CharField(max_length=255, widget=forms.PasswordInput)
	
class EnderecoForm(forms.Form):
	rua  =  forms.CharField(max_length=255)
	cidade = forms.CharField(max_length=255)
	bairro = forms.CharField(max_length=255)
	numero = forms.CharField(max_length=255)
	estado = forms.ChoiceField(choices=ESTADOS)

class CadastroModelForm(forms.ModelForm):
	rua  =  forms.CharField(max_length=255)
	cidade = forms.CharField(max_length=255)
	bairro = forms.CharField(max_length=255)
	numero = forms.CharField(max_length=255)
	email = forms.EmailField(max_length=255)
	senha = forms.CharField(max_length=255, widget=forms.PasswordInput)
	estado = forms.ChoiceField(choices=ESTADOS)

	class Meta:
		model = Cliente
		fields = ['nome', 'cpf', 'telefone']
		labels = {
		'nome': 'Nome Completo'
		}

	def clean(self):
		rua = self.cleaned_data.get('rua')
		cidade = self.cleaned_data.get('cidade')
		bairro = self.cleaned_data.get('bairro')
		numero = self.cleaned_data.get('numero')
		email = self.cleaned_data.get('email')
		senha = self.cleaned_data.get('senha')
		estado = self.cleaned_data.get('estado')

		novo_endereco = Endereco.objects.create(rua=rua, cidade=cidade, bairro=bairro, numero=numero)

		novo_usuario = User.objects.create_user(username=email,email=email,password=senha)

		self.cleaned_data['usuario'] = novo_usuario
		self.cleaned_data['endereco'] = novo_endereco
		return super(CadastroModelForm, self).clean()

class AnimalModelForm(forms.ModelForm):
	class Meta:
		model = Animal
		fields = ['foto','nome', 'sexo', 'especie', 'dono', 'idade']

class LoginForm(forms.Form):
	email = forms.EmailField(max_length=255)
	senha = forms.CharField(max_length=255, widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		user = User.objects.get(username=cleaned_data['email'])
		
		if user is not None:
			return cleaned_data

class AtendimentoForm(forms.Form):
	servico = forms.ChoiceField(choices=SERVICOS)
	animal = forms.ModelChoiceField(queryset=[], empty_label='Nothing')

	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(AtendimentoForm, self).__init__(*args, **kwargs)
		self.fields['animal'].queryset = self.user.cliente.animais.all()