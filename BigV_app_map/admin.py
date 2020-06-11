from django.contrib import admin
from BigV_app_map.forms import Dados_Mapeamento,Endereco


#Define a class admin

@admin.register(Dados_Mapeamento)                              # mesma coisa que isso admin.site.register(Dados_Mapeamento,Dados_admin)
class Dados_admin(admin.ModelAdmin):                           # para criar coluna no painel admin
    list_display = ('nome','site','email','cnpj') 

# Register your models here.

@admin.register(Endereco)
class Endereco_admin(admin.ModelAdmin):
    list_display = ('cep','rua','bairro','cidade','estado') 


