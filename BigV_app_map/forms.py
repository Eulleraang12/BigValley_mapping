from django.forms import ModelForm
from django import forms
from BigV_app_map.models import Dados_Mapeamento
from django.forms.widgets import TextInput,RadioSelect

class TransacaoForm_Dados(ModelForm):
    class Meta:
        model = Dados_Mapeamento
        fields = [ 'nome','site','email','cnpj',
                   'cep','rua','bairro','cidade','estado',
                   'nome_representante','cargo','telefone','email_representante', 
                   'industria','comercio','servico',
                   'area_de_atuacao_da_empresa_ou_startup','segmento_area','detalhes_de_area_de_atuacao','segmento_de_atuacao', 'tipo_de_cliente',
                   'possui_mercado_Global','possui_Influencia_ou_interesse_militar',
                   ]
                    #  
                
                
                               #valodar CNPJ e Email
        widgets = {
            'nome':  TextInput(attrs={'placeholder': 'Nome da Startup'}),
            'cnpj':  TextInput(attrs={'placeholder': ' xx.xxx.xxx/xxxx-xx'}),
            'site':  TextInput(attrs={'placeholder': 'http://www.seuwebsite.com'}),
            'email': TextInput(attrs={'placeholder': 'meuemail@qualquer.com'}),

            'cep': TextInput(attrs={'placeholder': 'xxxxx-xxx'}), ####### fazer Auto preenchimento com CEP
            
            'telefone': TextInput(attrs={'placeholder': '(xx)xxxxx-xxxx'}),

            'possui_mercado_Global': RadioSelect(),
            'possui_Influencia_ou_interesse_militar': RadioSelect(),
            }



    
    
