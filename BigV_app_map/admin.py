from django.contrib import admin
from BigV_app_map.models import Dados_Mapeamento


#Define a class admin

@admin.register(Dados_Mapeamento)                              # mesma coisa que isso admin.site.register(Dados_Mapeamento,Dados_admin)
class Dados_admin(admin.ModelAdmin):                           # para criar coluna no painel admin
    list_display = ('nome','site','email',
                    'rua','bairro','cidade') 
# Register your models here.     'cep',      'cnpj', ,'estado'


# admin.site.register(Dados_Mapeamento)
