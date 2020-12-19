from django.contrib import admin
from BigV_app_map.models import Dados_Mapeamento_startup,Dados_Mapeamento_empresa


#Define a class admin

@admin.register(Dados_Mapeamento_startup)                              # mesma coisa que isso admin.site.register(Dados_Mapeamento,Dados_admin)
class Dados_admin(admin.ModelAdmin):                           # para criar coluna no painel admin
    list_display = ('nome','site','email','telefone') #botar 'telefone' no lugar de cnpj depois
# Register your models here.     'cep',      'cnpj', ,'estado'


# admin.site.register(Dados_Mapeamento)

@admin.register(Dados_Mapeamento_empresa)                              # mesma coisa que isso admin.site.register(Dados_Mapeamento,Dados_admin)
class Dados_admin(admin.ModelAdmin):                           # para criar coluna no painel admin
    list_display = ('nome',) #'site','email','telefone'