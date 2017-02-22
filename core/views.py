from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadastroModelForm, AnimalModelForm, LoginForm, AtendimentoForm
from django.contrib.auth import authenticate, login as login_method
from django.contrib.auth import logout as logout_method

from django.views.generic import TemplateView, View

# Create your views here.

class HomeView(TemplateView):
	template_name = 'home.html'

class LoginView(View):
	form_class = LoginForm
	template_name = 'login.html'

	def get(self, request):
		form = self.form_class()
		return render(request, 'login.html', locals())

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['senha'])
			if user is not None:
				login_method(request, user)

				return redirect('cadastrar_animal')
			else:
				return redirect('home')

			return redirect('home')

		return render(request, 'login.html', locals())

def logout(request):
	logout_method(request)
	return redirect('home')

class CadastroView(View):
	form_class = CadastroModelForm
	template_name = 'cadastro.html'

	def get(self, request):
		form = self.form_class()
		return render(request, 'cadastro.html', locals())

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()

			return redirect('home')
		else:
			form = CadastroModelForm()

			texto='Coloque aqui seu nome'

		return render(request, 'cadastro.html', locals())

class AnimalView(View):
	form_class = AnimalModelForm
	template_name = 'animal.html'

	def get(self, request):
		form = self.form_class()
		return render(request, 'animal.html', locals())

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

		return render(request, 'animal.html', locals())

class AtendimentoView(View):
	template_name = 'atendimento.html'
	form_class = AtendimentoForm

	def get(self, request):
		form = self.form_class(request.user)
		return render(request, 'atendimento.html', locals())

	def post(self, request):
		form = self.form_class(request.user, request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

		return render(request, 'atendimento.html', locals())


