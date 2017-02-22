from django.contrib import admin
from .models import Animal
from .models import Cliente
from .models import Endereco

# Register your models here.
class AnimalInline(admin.TabularInline):
	model = Animal

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cpf')
	inlines = [AnimalInline, ]

class AnimalAdmin(admin.ModelAdmin):
	list_display = ('nome', 'dono')

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco)